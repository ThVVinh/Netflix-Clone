package com.netflixclone.backend.entity.MultiAttributeKey;

public class MovieGenreKey implements java.io.Serializable {
    private Long movieId;
    private Long genreId;

    public MovieGenreKey() {}

    public MovieGenreKey(Long movieId, Long genreId) {
        this.movieId = movieId;
        this.genreId = genreId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof MovieGenreKey)) return false;
        MovieGenreKey that = (MovieGenreKey) o;
        return movieId.equals(that.movieId) &&
               genreId.equals(that.genreId);
    }

    @Override
    public int hashCode() {
        return java.util.Objects.hash(movieId, genreId);
    }
    
}
