package com.netflixclone.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.netflixclone.backend.entity.TransactionDetail;
import com.netflixclone.backend.entity.MultiAttributeKey.TransactionDetailKey;

@Repository
public interface TransactionDetailRepo extends JpaRepository<TransactionDetail, TransactionDetailKey> {

    
}
