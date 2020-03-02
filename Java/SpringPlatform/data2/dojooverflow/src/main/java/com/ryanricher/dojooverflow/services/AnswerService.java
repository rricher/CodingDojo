package com.ryanricher.dojooverflow.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.dojooverflow.models.Answer;
import com.ryanricher.dojooverflow.repositories.AnswerRepository;

@Service
public class AnswerService {
	private final AnswerRepository answerRepo;
	public AnswerService(AnswerRepository answerRepo) {
		this.answerRepo = answerRepo;
	}

	public Answer findOne(Long id) {
		Optional<Answer> x = answerRepo.findById(id);
		if(x.isPresent()) {
			return x.get();
		} else {
			return null;
		}
	}
}
