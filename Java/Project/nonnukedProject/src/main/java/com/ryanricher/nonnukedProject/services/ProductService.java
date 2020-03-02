package com.ryanricher.nonnukedProject.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.nonnukedProject.models.Product;
import com.ryanricher.nonnukedProject.repositories.ProductRepository;

@Service
public class ProductService {
    private final ProductRepository prepo;
    
    public ProductService(ProductRepository prepo) {
        this.prepo = prepo;
    }
  
    // find user by id
    public Product findUserById(Long id) {
    	Optional<Product> u = prepo.findById(id);
    	
    	if(u.isPresent()) {
            return u.get();
    	} else {
    	    return null;
    	}
    }
}