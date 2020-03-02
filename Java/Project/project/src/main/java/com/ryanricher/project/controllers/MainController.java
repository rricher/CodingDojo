package com.ryanricher.project.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.ryanricher.project.models.Product;
import com.ryanricher.project.models.User;
import com.ryanricher.project.repositories.CategoryRepository;
import com.ryanricher.project.repositories.ProductRepository;
import com.ryanricher.project.repositories.UserRepository;
import com.ryanricher.project.services.CategoryService;
import com.ryanricher.project.services.ProductService;
import com.ryanricher.project.services.UserService;
import com.ryanricher.project.validators.UserValidator;

@Controller
public class MainController {
	
	private final UserRepository urepo;
	private final UserService userv;
	private final UserValidator uval;
	private final ProductRepository prepo;
	private final ProductService pserv;
	private final CategoryRepository crepo;
	private final CategoryService cserv;
	
	
	
	public MainController(UserRepository urepo, UserService userv, UserValidator uval, ProductRepository prepo,
			ProductService pserv, CategoryRepository crepo, CategoryService cserv) {
		this.urepo = urepo;
		this.userv = userv;
		this.uval = uval;
		this.prepo = prepo;
		this.pserv = pserv;
		this.crepo = crepo;
		this.cserv = cserv;
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
        return "redirect:/dash";
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
	
	@GetMapping("/dash")
	public String dashboard(Model model) {
		model.addAttribute("products", prepo.findAll());
		return "dashboard.jsp";
	}
	
	@GetMapping("/new")
	public String newProduct(Model model) {
		model.addAttribute("product", new Product());
		model.addAttribute("categories", crepo.findAll());
		return "newProduct.jsp";
	}
	
	@PostMapping("/new")
	public String createProduct(@Valid @ModelAttribute("product") Product product, BindingResult result, HttpSession session) {
		if(result.hasErrors()) {
			return "newProduct.jsp";
		} else {
			prepo.save(product);
			return "redirect:/dash";
		}
	}
}
