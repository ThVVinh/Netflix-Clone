package com.netflixclone.backend.entity.MultiAttributeKey;

public class OwnedMovieKey implements java.io.Serializable {
    private Long userId;
    private Long movieId;

    public OwnedMovieKey() {}

    public OwnedMovieKey(Long userId, Long movieId) {
        this.userId = userId;
        this.movieId = movieId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof OwnedMovieKey)) return false;
        OwnedMovieKey that = (OwnedMovieKey) o;
        return userId.equals(that.userId) &&
               movieId.equals(that.movieId);
    }

    @Override
    public int hashCode() {
        return java.util.Objects.hash(userId, movieId);
    }
}