package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.Movie;

@Repository
public interface MovieRepo extends JpaRepository<Movie, Long> {

    
}
