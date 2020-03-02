package com.example.demo.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.example.demo.models.Show;
import com.example.demo.repositories.ShowRepo;

@Service
public class ShowServ {
	private final ShowRepo srepo;
	public ShowServ(ShowRepo srepo) {
		this.srepo = srepo;
	}
	public Show findOne(Long id) {
		Optional<Show> s = srepo.findById(id);
		if(s.isPresent()) {
			return s.get();
		} else {
			return null;
		}
	}
}
