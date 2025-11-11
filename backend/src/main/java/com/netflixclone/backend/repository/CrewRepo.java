package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.Crew;

@Repository
public interface CrewRepo extends JpaRepository<Crew, Long> {

    
}
