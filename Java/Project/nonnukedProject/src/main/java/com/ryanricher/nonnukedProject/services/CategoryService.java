package com.ryanricher.nonnukedProject.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.nonnukedProject.models.Category;
import com.ryanricher.nonnukedProject.repositories.CategoryRepository;

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