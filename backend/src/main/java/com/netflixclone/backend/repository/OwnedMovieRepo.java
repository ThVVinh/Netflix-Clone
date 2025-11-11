package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.OwnedMovie;
import com.netflixclone.backend.entity.MultiAttributeKey.OwnedMovieKey;

@Repository
public interface OwnedMovieRepo extends JpaRepository<OwnedMovie, OwnedMovieKey> {

    
}