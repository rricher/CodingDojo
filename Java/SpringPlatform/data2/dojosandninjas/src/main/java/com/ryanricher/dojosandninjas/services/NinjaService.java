package com.ryanricher.dojosandninjas.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.dojosandninjas.models.Ninja;
import com.ryanricher.dojosandninjas.repositories.NinjaRepository;

@Service
public class NinjaService {
	private final NinjaRepository ninjaRepo;
	public NinjaService(NinjaRepository ninjaRepo) {
		this.ninjaRepo = ninjaRepo;
	}

	public Ninja findOne(Long id) {
		Optional<Ninja> x = ninjaRepo.findById(id);
		if(x.isPresent()) {
			return x.get();
		} else {
			return null;
		}
	}
}
