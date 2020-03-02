package com.ryanricher.project.services;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.project.models.Product;
import com.ryanricher.project.repositories.ProductRepository;

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