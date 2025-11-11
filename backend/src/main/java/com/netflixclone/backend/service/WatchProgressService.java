package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.WatchProgress;
import com.netflixclone.backend.repository.WatchProgressRepo;

@Service
public class WatchProgressService {
    private final WatchProgressRepo watchProgressRepo;

    public WatchProgressService(WatchProgressRepo watchProgressRepo) {
        this.watchProgressRepo = watchProgressRepo;
    }

    public WatchProgress getWatchProgressById(Long id) {
        return watchProgressRepo.findById(id).orElse(null);
    }

    public WatchProgress saveWatchProgress(WatchProgress watchProgress) {
        return watchProgressRepo.save(watchProgress);
    }

    public void deleteWatchProgress(Long id) {
        watchProgressRepo.deleteById(id);
    }

    public List<WatchProgress> getAllWatchProgresses() {
        return watchProgressRepo.findAll();
    }
}
