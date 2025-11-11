package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.Transaction;

@Repository
public interface TransactionRepo extends JpaRepository<Transaction, Long> {

    
}
