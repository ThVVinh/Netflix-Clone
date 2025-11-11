package com.netflixclone.backend.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.repository.MediaRepo;
import com.netflixclone.backend.entity.Media;

@Service
public class MediaService {
    private final MediaRepo mediaRepo;

    public MediaService(MediaRepo mediaRepo) {
        this.mediaRepo = mediaRepo;
    }

    public List<Media> getAllMedia() {
        return mediaRepo.findAll();
    }

    public Media getMediaById(Long id) {
        return mediaRepo.findById(id).orElse(null);
    }

    public Media saveMedia(Media media) {
        return mediaRepo.save(media);
    }

    public void deleteMedia(Long id) {
        mediaRepo.deleteById(id);
    }
    
}
