package com.example.demo.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.models.Show;

@Repository
public interface ShowRepo extends CrudRepository<Show, Long> {
	List<Show> findAll();
	List<Show> findByTitleContaining(String search);
	List<Show> findByNetworkContaining(String search);
}
