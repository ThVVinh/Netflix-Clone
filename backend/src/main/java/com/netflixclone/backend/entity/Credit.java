package com.netflixclone.backend.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "credit")
public class Credit {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "movie_id")
    private Long movieId;

    @Column(name = "people_id")
    private Long peopleId;

    @Column(name = "department")
    private String department;

    @Column(name = "credit_type")
    private String creditType;

    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public Long getMovieId() {
        return movieId;
    }
    public void setMovieId(Long movieId) {
        this.movieId = movieId;
    }
    public Long getPeopleId() {
        return peopleId;
    }
    public void setPeopleId(Long peopleId) {
        this.peopleId = peopleId;
    }
    public String getDepartment() {
        return department;
    }
    public void setDepartment(String department) {
        this.department = department;
    }
    public String getCreditType() {
        return creditType;
    }
    public void setCreditType(String creditType) {
        this.creditType = creditType;
    }
    
}
