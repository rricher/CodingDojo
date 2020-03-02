package com.ryanricher.project.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.ryanricher.project.models.Product;


@Repository
public interface ProductRepository extends CrudRepository<Product, Long> {
    Product findByName(String name);
    List<Product> findAll();
}