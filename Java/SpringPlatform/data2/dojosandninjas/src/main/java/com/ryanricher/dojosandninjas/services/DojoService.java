package com.ryanricher.dojosandninjas.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.dojosandninjas.models.Dojo;
import com.ryanricher.dojosandninjas.repositories.DojoRepository;

@Service
public class DojoService {
	private final DojoRepository dojoRepo;
	public DojoService(DojoRepository dojoRepo) {
		this.dojoRepo = dojoRepo;
	}

	public Dojo findOne(Long id) {
		Optional<Dojo> x = dojoRepo.findById(id);
		if(x.isPresent()) {
			return x.get();
		} else {
			return null;
		}
	}
}
