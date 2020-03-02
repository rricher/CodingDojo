package com.ryanricher.dojooverflow.controllers;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.ryanricher.dojooverflow.models.Question;
import com.ryanricher.dojooverflow.repositories.AnswerRepository;
import com.ryanricher.dojooverflow.repositories.QuestionRepository;
import com.ryanricher.dojooverflow.repositories.TagRepository;
import com.ryanricher.dojooverflow.services.AnswerService;
import com.ryanricher.dojooverflow.services.QuestionService;
import com.ryanricher.dojooverflow.services.TagService;
import com.ryanricher.mvc.models.Book;

@Controller
public class MainController {

	private final QuestionRepository questRepo;
	private final QuestionService questServ;
	private final AnswerRepository answerRepo;
	private final AnswerService answerServ;
	private final TagRepository tagRepo;
	private final TagService tagServ;
	
	public MainController(QuestionRepository questRepo, QuestionService questServ, AnswerRepository answerRepo,
			AnswerService answerServ, TagRepository tagRepo, TagService tagServ) {
		this.questRepo = questRepo;
		this.questServ = questServ;
		this.answerRepo = answerRepo;
		this.answerServ = answerServ;
		this.tagRepo = tagRepo;
		this.tagServ = tagServ;
	}
	
	@GetMapping("/questions")
	public String questions(Model model) {
		model.addAttribute("questions", questRepo.findAll());
		return "questions.jsp";
	}
	
	@GetMapping("/questions/new")
	public String newQuest(Model model) {
		model.addAttribute("question", new Question());
		return "newQuestion.jsp";
	}
	
	@PostMapping("/questions/new")
	public String postQuest(Model model, @Valid @ModelAttribute("question") Question question, BindingResult result) {
		for(tag:Tags) {
			
		}
		System.out.println(question.getTags().get(0));
		return "redirect/questions/new";
	}
	
}

