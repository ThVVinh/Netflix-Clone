package com.netflixclone.backend.entity;

import com.netflixclone.backend.entity.MultiAttributeKey.MovieGenreKey;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.Table;

@Entity
@IdClass(MovieGenreKey.class)
@Table(name = "movie_genre")
public class MovieGenre {
    @Id
    @Column(name = "movie_id")
    private Long movieId;

    @Id
    @Column(name = "genre_id")
    private Long genreId;

    public Long getMovieId() {
        return movieId;
    }
    public void setMovieId(Long movieId) {
        this.movieId = movieId;
    }
    public Long getGenreId() {
        return genreId;
    }
    public void setGenreId(Long genreId) {
        this.genreId = genreId;
    }
}
