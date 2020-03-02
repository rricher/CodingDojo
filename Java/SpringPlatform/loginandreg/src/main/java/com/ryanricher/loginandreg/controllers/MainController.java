package com.ryanricher.loginandreg.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.ryanricher.loginandreg.models.User;
import com.ryanricher.loginandreg.repositories.UserRepository;
import com.ryanricher.loginandreg.services.UserService;
import com.ryanricher.loginandreg.validators.UserValidator;

@Controller
public class MainController {
	
	private final UserRepository urepo;
	private final UserService userv;
	private final UserValidator uval;
	
	public MainController(UserRepository urepo, UserService userv, UserValidator uval) {
		this.urepo = urepo;
		this.userv = userv;
		this.uval = uval;
	}
	
	@GetMapping("/")
	public String index(Model model)  {
		model.addAttribute("user", new User());
		return "index.jsp";
	}
	
	@PostMapping("/registration")
    public String registration(@Valid @ModelAttribute("user") User user, BindingResult result, HttpSession session) {
        uval.validate(user, result);
        if(result.hasErrors()) {
            return "index.jsp";
        }
        User u = userv.registerUser(user);
        session.setAttribute("userId", u.getId());
        return "redirect:/home";
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
}
