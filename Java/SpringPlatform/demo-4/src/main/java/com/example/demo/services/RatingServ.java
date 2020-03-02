package com.example.demo.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.example.demo.models.Rating;
import com.example.demo.repositories.RatingRepo;

@Service
public class RatingServ {
	private final RatingRepo rrepo;
	public RatingServ(RatingRepo rrepo) {
		this.rrepo = rrepo;
	}
	public Rating findOne(Long id) {
		Optional<Rating> r = rrepo.findById(id);
		if(r.isPresent()) {
			return r.get();
		} else {
			return null;
		}
	}
}
