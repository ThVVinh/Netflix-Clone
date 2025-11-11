package com.netflixclone.backend.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.Table;
import com.netflixclone.backend.entity.MultiAttributeKey.OwnedMovieKey;

@Entity
@IdClass(OwnedMovieKey.class)
@Table(name = "owned_movies") 
public class OwnedMovie {
    @Id
    @Column(name = "user_id")
    private Long userId;
    
    @Id
    @Column(name = "movie_id")
    private Long movieId;
    
    public Long getUserId() {
        return userId;
    }
    public void setUserId(Long userId) {
        this.userId = userId;
    }
    public Long getMovieId() {
        return movieId;
    }
    public void setMovieId(Long movieId) {
        this.movieId = movieId;
    }
}
