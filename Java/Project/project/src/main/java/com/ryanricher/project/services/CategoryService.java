package com.ryanricher.project.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.project.models.Category;
import com.ryanricher.project.repositories.CategoryRepository;

@Service
public class CategoryService {
    private final CategoryRepository crepo;
    
    public CategoryService(CategoryRepository crepo) {
        this.crepo = crepo;
    }
  
    // find user by id
    public Category findUserById(Long id) {
    	Optional<Category> u = crepo.findById(id);
    	
    	if(u.isPresent()) {
            return u.get();
    	} else {
    	    return null;
    	}
    }
}