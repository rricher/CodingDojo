package com.ryanricher.dojooverflow.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.dojooverflow.models.Question;
import com.ryanricher.dojooverflow.repositories.QuestionRepository;

@Service
public class QuestionService {
	private final QuestionRepository questRepo;
	public QuestionService(QuestionRepository questRepo) {
		this.questRepo = questRepo;
	}

	public Question findOne(Long id) {
		Optional<Question> x = questRepo.findById(id);
		if(x.isPresent()) {
			return x.get();
		} else {
			return null;
		}
	}
}
