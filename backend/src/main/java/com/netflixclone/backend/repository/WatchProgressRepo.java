package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.WatchProgress;

@Repository
public interface WatchProgressRepo extends JpaRepository<WatchProgress, Long> {

    
}
