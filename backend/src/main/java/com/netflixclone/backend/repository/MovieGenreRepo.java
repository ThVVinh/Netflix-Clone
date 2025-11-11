package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.MovieGenre;
import com.netflixclone.backend.entity.MultiAttributeKey.MovieGenreKey;

@Repository
public interface MovieGenreRepo extends JpaRepository<MovieGenre, MovieGenreKey> {

    
} 
