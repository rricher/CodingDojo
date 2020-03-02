package com.ryanricher.dojooverflow.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.dojooverflow.models.Tag;
import com.ryanricher.dojooverflow.repositories.TagRepository;

@Service
public class TagService {
	private final TagRepository tagRepo;
	public TagService(TagRepository tagRepo) {
		this.tagRepo = tagRepo;
	}

	public Tag findOne(Long id) {
		Optional<Tag> x = tagRepo.findById(id);
		if(x.isPresent()) {
			return x.get();
		} else {
			return null;
		}
	}
}
