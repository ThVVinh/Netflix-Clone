package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.Movie;
import com.netflixclone.backend.repository.MovieRepo;

@Service
public class MovieService {
    private final MovieRepo movieRepo;

    public MovieService(MovieRepo movieRepo) {
        this.movieRepo = movieRepo;
    }

    public List<Movie> getAllMovies() {
        return movieRepo.findAll();
    }

    public Movie getMovieById(Long id) {
        return movieRepo.findById(id).orElse(null);
    }

    public Movie saveMovie(Movie movie) {
        return movieRepo.save(movie);
    }

    public void deleteMovie(Long id) {
        movieRepo.deleteById(id);
    }
}
