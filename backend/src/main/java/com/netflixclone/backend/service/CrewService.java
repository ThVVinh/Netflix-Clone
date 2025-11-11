package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.Crew;
import com.netflixclone.backend.repository.CrewRepo;

@Service
public class CrewService {
    private final CrewRepo crewRepo;

    public CrewService(CrewRepo crewRepo) {
        this.crewRepo = crewRepo;
    }

    public Crew getCrewById(Long id) {
        return crewRepo.findById(id).orElse(null);
    }

    public Crew saveCrew(Crew crew) {
        return crewRepo.save(crew);
    }

    public void deleteCrew(Long id) {
        crewRepo.deleteById(id);
    }

    public List<Crew> getAllCrews() {
        return crewRepo.findAll();
    }
}
