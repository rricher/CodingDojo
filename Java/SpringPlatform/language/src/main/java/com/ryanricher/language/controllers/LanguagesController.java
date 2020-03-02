package com.ryanricher.language.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.ryanricher.language.models.Language;
import com.ryanricher.language.repositories.LanguageRepository;
import com.ryanricher.language.services.LanguageService;

@Controller
public class LanguagesController {
	private final LanguageService languageService;
	private final LanguageRepository languageRepository;
	
	public LanguagesController(LanguageService languageService, LanguageRepository languageRepository) {
		this.languageService = languageService;
		this.languageRepository = languageRepository;
	}
	
	@GetMapping("/languages")
	public String showAll(Model model) {
		List<Language> languages = languageService.allLanguages();
		model.addAttribute("languages", languages);
		model.addAttribute("language", new Language());
		return "/languages/index.jsp";
	}
	
	@PostMapping("/languages")
	public String createLanguage(Model model, @Valid @ModelAttribute("language") Language language, BindingResult result) {
		if (result.hasErrors()) {
			List<Language> languages = languageService.allLanguages();
			model.addAttribute("languages", languages);
			return "/languages/index.jsp";
		} else {
			languageRepository.save(language);
			return "redirect:/languages";
		}
	}
	
	@GetMapping("/languages/{lang_id}/delete")
	public String deleteLanguage(@PathVariable("lang_id") Long id) {
		languageRepository.deleteById(id);
		return "redirect:/languages";
	}
	
	@GetMapping("/languages/{lang_id}")
	public String showBook(Model model, @PathVariable("lang_id") Long id) {
		Language language = languageService.findBook(id);
		model.addAttribute("language", language);
		return "/languages/show.jsp";
	}
	
	@GetMapping("/languages/{lang_id}/edit")
	public String editBook(Model model, @PathVariable("lang_id") Long id) {
		Language language = languageService.findBook(id);
		model.addAttribute("language", language);
		return "/languages/edit.jsp";
	}
	
	@PostMapping("/languages/{lang_id}/edit")
	public String postBook(@PathVariable("lang_id") Long id,  @Valid @ModelAttribute("book") Language language, BindingResult result) {
		if (result.hasErrors()) {
			language.setId(id);
			return "languages/edit.jsp";
		} else {
			language.setId(id);
			languageRepository.save(language);
			return "redirect:/languages/" + id;
		}
	}

}
