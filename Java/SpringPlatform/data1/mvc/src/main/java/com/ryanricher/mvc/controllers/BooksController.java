package com.ryanricher.mvc.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.ryanricher.mvc.models.Book;
import com.ryanricher.mvc.repositories.BookRepository;
import com.ryanricher.mvc.services.BookService;

@Controller
public class BooksController {
    private final BookService bookService;
    private final BookRepository bookRepository;
    
    public BooksController(BookService bookService,BookRepository bookRepository) {
        this.bookService = bookService;
        this.bookRepository = bookRepository;
    }
    
    @RequestMapping("/books")
    public String index(Model model) {
        List<Book> books = bookService.allBooks();
        model.addAttribute("books", books);
        return "/books/index.jsp";
    }
    
    @RequestMapping("/books/{book_id}")
    public String show(@PathVariable("book_id") Long id, Model model) {
    	Book book = bookService.findBook(id);
    	model.addAttribute("book", book);
    	return "/books/show.jsp";
    }
    
    @RequestMapping("/books/{book_id}/edit")
    public String edit(@PathVariable("book_id") Long id, Model model) {
    	Book book = bookService.findBook(id);
    	model.addAttribute("book", book);
    	return "/books/edit.jsp";
    }
    
    @RequestMapping(value="/books/{book_id}/edit", method=RequestMethod.POST)
    public String edit(@PathVariable("book_id") Long id, @Valid @ModelAttribute("book") Book book, BindingResult result) {
        if (result.hasErrors()) {
        	book.setId(id);
            return "redirect:/books/" + id + "/edit/";
        } else {
            book.setId(id);
            bookRepository.save(book);
            return "redirect:/books/" + id;
        }
    }
    
    @RequestMapping("/books/new")
    public String newBook(@ModelAttribute("book") Book book) {
        return "/books/new.jsp";
    }
    @PostMapping("/books")
    public String create(@Valid @ModelAttribute("book") Book book, BindingResult result) {
        if (result.hasErrors()) {
            return "/books/new.jsp";
        } else {
            bookService.createBook(book);
            return "redirect:/books";
        }
    }
    
    @RequestMapping(value="/books/{id}", method=RequestMethod.DELETE)
    public String destroy(@PathVariable("id") Long id) {
        bookService.deleteBook(id);
        return "redirect:/books";
    }
}