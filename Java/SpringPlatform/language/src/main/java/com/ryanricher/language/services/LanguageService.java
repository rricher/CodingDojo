package com.ryanricher.language.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.ryanricher.language.models.Language;
import com.ryanricher.language.repositories.LanguageRepository;

@Service
public class LanguageService {
	
	private final LanguageRepository languageRepository;
	
	public LanguageService(LanguageRepository languageRepository) {
		this.languageRepository = languageRepository;
	}
	
	// returns all the books
    public List<Language> allLanguages() {
        return languageRepository.findAll();
    }
    // creates a book
    public Language createBook(Language l) {
        return languageRepository.save(l);
    }
    // retrieves a book
    public Language findBook(Long id) {
        Optional<Language> optionalLanguage = languageRepository.findById(id);
        if(optionalLanguage.isPresent()) {
            return optionalLanguage.get();
        } else {
            return null;
        }
    }
}
