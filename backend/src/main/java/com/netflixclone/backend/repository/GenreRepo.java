package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.Genre;

@Repository
public interface GenreRepo extends JpaRepository<Genre, Long> {

    
}
