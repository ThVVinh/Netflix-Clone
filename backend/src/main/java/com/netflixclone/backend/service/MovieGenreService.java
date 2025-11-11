package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.MovieGenre;
import com.netflixclone.backend.entity.MultiAttributeKey.MovieGenreKey;
import com.netflixclone.backend.repository.MovieGenreRepo;

@Service
public class MovieGenreService {
    private final MovieGenreRepo movieGenreRepo;

    public MovieGenreService(MovieGenreRepo movieGenreRepo) {
        this.movieGenreRepo = movieGenreRepo;
    }

    public List<MovieGenre> getAllMovieGenres() {
        return movieGenreRepo.findAll();
    }

    public MovieGenre getMovieGenreById(Long movieId, Long genreId) {
        MovieGenreKey key = new MovieGenreKey(movieId, genreId);
        return movieGenreRepo.findById(key).orElse(null);
    }

    public MovieGenre saveMovieGenre(MovieGenre movieGenre) {
        return movieGenreRepo.save(movieGenre);
    }

    public void deleteMovieGenre(Long movieId, Long genreId) {
        MovieGenreKey key = new MovieGenreKey(movieId, genreId);
        movieGenreRepo.deleteById(key);
    }
}
