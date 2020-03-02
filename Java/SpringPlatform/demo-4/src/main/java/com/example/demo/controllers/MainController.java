package com.example.demo.controllers;

import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.models.Rating;
import com.example.demo.models.Show;
import com.example.demo.models.User;
import com.example.demo.repositories.RatingRepo;
import com.example.demo.repositories.ShowRepo;
import com.example.demo.repositories.UserRepo;
import com.example.demo.services.RatingServ;
import com.example.demo.services.ShowServ;
import com.example.demo.services.UserServ;
import com.example.demo.validators.UserValidator;

@Controller
public class MainController {
	private final UserRepo urepo;
	private final UserServ userv;
	private final ShowRepo srepo;
	private final ShowServ sserv;
	private final RatingRepo rrepo;
	private final RatingServ rserv;
    private final UserValidator userValidator;

	public MainController(
			UserRepo urepo,
			UserServ userv,
			ShowRepo srepo,
			ShowServ sserv,
			RatingRepo rrepo,
			RatingServ rserv,
			UserValidator userValidator
			) {
		this.urepo = urepo;
		this.userv = userv;
		this.srepo = srepo;
		this.sserv = sserv;
		this.rrepo = rrepo;
		this.rserv = rserv;
        this.userValidator = userValidator;

	}
	// Login and Registration
	@GetMapping("/")
	public String index(Model model) {
		model.addAttribute("user", new User());
		return "index.jsp";
	}
	
	@PostMapping("/registration")
    public String registerUser(@Valid @ModelAttribute("user") User user, BindingResult result, HttpSession session) {
        userValidator.validate(user, result);
		if(result.hasErrors()) {
			return "index.jsp";
		} else {
			User u = userv.registerUser(user);
			session.setAttribute("userid", u.getId());
			return "redirect:/dash";
		}
    }
	
	@PostMapping("/login")
    public String loginUser(@RequestParam("email") String email, @RequestParam("password") String password, Model model, HttpSession session) {
		if(userv.authenticateUser(email, password)) {
			User u = urepo.findByEmail(email);
			session.setAttribute("userid", u.getId());
			return "redirect:/dash";
		} else {
			model.addAttribute("user", new User());
			model.addAttribute("error", "Invalid login");
			return "index.jsp";
		}
        
    }
	
	@GetMapping("/logout")
	public String logoutUser(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
	
	// *************************
	
	@GetMapping("/dash")
	public String dashboard(Model model) {
		List<Show> shows = srepo.findAll();
		model.addAttribute("shows", shows);
		
		for(int i = 0; i < shows.size(); i++) {
			Show show = shows.get(i);
			float sum = 0;
			for(int j = 0; j < show.getRatings().size(); j++) {
				Rating rating = show.getRatings().get(j);
				sum += rating.getRate();
			}
			float average = sum / show.getRatings().size();
			shows.get(i).setAverage(average);
		}
		return "dash.jsp";
	}
	
	@GetMapping("/new/show")
	public String newShow(Model model, HttpSession session) {
		model.addAttribute("show", new Show());
		return "new.jsp";
	}
	
	@PostMapping("/new/show")
	public String createShow(@Valid @ModelAttribute("show") Show show, BindingResult result, HttpSession session) {
		if(result.hasErrors()) {
			return "new.jsp";
		} else {
			Long uid = (Long) session.getAttribute("userid");
			User u = userv.findOne(uid);
			show.setCreator(u);
			srepo.save(show);
			return "redirect:/dash";
		}
	}
	
	@GetMapping("/delete/{showid}")
	public String deleteShow(@PathVariable("showid") Long showid) {
		srepo.deleteById(showid);
		return "redirect:/dash";
	}
	
	@GetMapping("/edit/{showid}")
	public String editShow(HttpSession session, Model model, @PathVariable("showid") Long showid) {
		Long uid = (Long) session.getAttribute("userid");
		User u = userv.findOne(uid);
		
		Show show = sserv.findOne(showid);
		if(show.getCreator().equals(u)) {
			model.addAttribute("show", show);
			return "edit.jsp";
		} else {
			return "redirect:/dash";
		}
		
	}
	
	@PostMapping("/edit/{showid}")
	public String changeShow(HttpSession session, @Valid @ModelAttribute("show") Show show, BindingResult result, @PathVariable("showid") Long showid) {
		if(result.hasErrors()) {
			show.setId(showid);
			return "edit.jsp";
		} else {
			show.setId(showid);
			Long uid = (Long) session.getAttribute("userid");
			User u = userv.findOne(uid);
			show.setCreator(u);
			srepo.save(show);
			return "redirect:/dash";
		}
	}
	
	@GetMapping("/show/{showid}")
	public String readShow(Model model, @PathVariable("showid") Long showid) {
		Show show = sserv.findOne(showid);
		model.addAttribute("show", show);
		model.addAttribute("rating", new Rating());
		return "show.jsp";
	}
	
	@PostMapping("/rateshow/{showid}")
	public String rateShow(Model model, @PathVariable("showid") Long showid, HttpSession session, @Valid @ModelAttribute("rating") Rating rating, BindingResult result) {
		if(result.hasErrors()) {
			Show show = sserv.findOne(showid);
			model.addAttribute("show", show);
			return "show.jsp";
		} else {
			
			// find the user,
			Long uid = (Long) session.getAttribute("userid");
			User u = userv.findOne(uid);
			//find the show, 
			Show show = sserv.findOne(showid);
			
			List<Rating> list = show.getRatings();
			for(int i = 0; i < list.size(); i++) {
				User rater = list.get(i).getRater();
				if(rater.equals(u)) {
					model.addAttribute("show", show);
					model.addAttribute("duplicate", "You already rated this show");
					return "show.jsp";
				}
			}
			//attach both to the rating,
			rating.setRater(u);
			rating.setRatedShow(show);
			//save the rating
			rrepo.save(rating);
			return "redirect:/show/" + showid;
		}
	}
	@GetMapping("/delete/rating/{ratingid}/{showid}")
	public String deleteRating(@PathVariable("showid") Long showid,@PathVariable("ratingid") Long rid) { 
		rrepo.deleteById(rid);
		return "redirect:/show/" + showid;
	}
	
	
}
