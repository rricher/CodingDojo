package com.ryanricher.dojosandninjas.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.ryanricher.dojosandninjas.models.Dojo;
import com.ryanricher.dojosandninjas.models.Ninja;
import com.ryanricher.dojosandninjas.repositories.DojoRepository;
import com.ryanricher.dojosandninjas.repositories.NinjaRepository;
import com.ryanricher.dojosandninjas.services.DojoService;
import com.ryanricher.dojosandninjas.services.NinjaService;

@Controller
public class MainController {
	private final DojoRepository dojoRepo;
	public final DojoService dojoServ;
	private final NinjaRepository ninjaRepo;
	public final NinjaService ninjaServ;
	
	public MainController(DojoRepository dojoRepo, DojoService dojoServ, NinjaRepository ninjaRepo,
			NinjaService ninjaServ) {
		this.dojoRepo = dojoRepo;
		this.dojoServ = dojoServ;
		this.ninjaRepo = ninjaRepo;
		this.ninjaServ = ninjaServ;
	}

	@GetMapping("/")
	public String index(Model model) {
		List<Dojo> myDojos = dojoRepo.findAll();
		model.addAttribute("myDojos", myDojos);
		List<Ninja> myNinjas = ninjaRepo.findAll();
		model.addAttribute("myNinjas", myNinjas);
		return "index.jsp";
	}
	
	@GetMapping("/dojos/new")
	public String newDojo(Model model) {
		model.addAttribute("dojo", new Dojo());
		return "newDojo.jsp";
	}
	
	@PostMapping("/dojos/new")
	public String postNewDojo(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result) {
		if(result.hasErrors()) {
			return "newDojo.jsp";
		} else {
			dojoRepo.save(dojo);
			return "redirect:/";
		}
	}
	
	@GetMapping("/ninjas/new")
	public String newNinja(Model model) {
		List<Dojo> dojos = dojoRepo.findAll();
		model.addAttribute("dojos", dojos);
		model.addAttribute("ninja", new Ninja());
		return "newNinja.jsp";
	}
	
	@PostMapping("/ninjas/new")
	public String postNewNinja(@Valid @ModelAttribute("ninja") Ninja ninja, BindingResult result, Model model) {
		if(result.hasErrors()) {
			List<Dojo> dojos = dojoRepo.findAll();
			model.addAttribute("dojos", dojos);
			return "newNinja.jsp";
		} else {
			ninjaRepo.save(ninja);
			return "redirect:/";
		}
	}
	
	@GetMapping("/dojos/{dojo_id}")
	public String showDojo(@PathVariable("dojo_id") Long id, Model model) {
		Dojo dojo = dojoServ.findOne(id);
		List<Ninja> ninjas = dojo.getNinjas();
		model.addAttribute("dojo", dojo);
		model.addAttribute("ninjas", ninjas);
		return "showDojo.jsp";
	}
}