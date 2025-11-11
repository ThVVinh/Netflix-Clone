package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.Review;
import com.netflixclone.backend.repository.ReviewRepo;

@Service
public class ReviewService {
    private final ReviewRepo reviewRepo;

    public ReviewService(ReviewRepo reviewRepo) {
        this.reviewRepo = reviewRepo;
    }

    public List<Review> getAllReviews() {
        return reviewRepo.findAll();
    }   

    public Review getReviewById(Long id) {
        return reviewRepo.findById(id).orElse(null);
    }   

    public Review saveReview(Review review) {
        return reviewRepo.save(review);
    }
    
    public void deleteReview(Long id) {
        reviewRepo.deleteById(id);
    }
}
