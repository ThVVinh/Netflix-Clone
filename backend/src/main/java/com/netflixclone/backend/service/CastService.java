package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.Cast;
import com.netflixclone.backend.repository.CastRepo;

@Service
public class CastService {
    private final CastRepo castRepo;

    public CastService(CastRepo castRepo) {
        this.castRepo = castRepo;
    }

    public Cast getCastById(Long id) {
        return castRepo.findById(id).orElse(null);
    }

    public Cast saveCast(Cast cast) {
        return castRepo.save(cast);
    }

    public void deleteCast(Long id) {
        castRepo.deleteById(id);
    }

    public List<Cast> getAllCasts() {
        return castRepo.findAll();
    }
}
