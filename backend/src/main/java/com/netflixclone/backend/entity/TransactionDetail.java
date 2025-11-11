package com.netflixclone.backend.entity;


import com.netflixclone.backend.entity.MultiAttributeKey.TransactionDetailKey;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.Table;


@Entity
@IdClass(TransactionDetailKey.class)
@Table(name = "transaction_details")
public class TransactionDetail {
    @Id
    @Column(name = "transaction_id")
    private Long transactionId;

    @Id
    @Column(name = "movie_id")
    private Long movieId;
    
    @Column(name = "price")
    private Double price;
    
    public Long getTransactionId() {
        return transactionId;
    }
    public void setTransactionId(Long transactionId) {
        this.transactionId = transactionId;
    }
    public Long getMovieId() {
        return movieId;
    }
    public void setMovieId(Long movieId) {
        this.movieId = movieId;
    }
    public Double getPrice() {
        return price;
    }
    public void setPrice(Double price) {
        this.price = price;
    }

}
