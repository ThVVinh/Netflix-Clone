package com.netflixclone.backend.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.netflixclone.backend.entity.User;
import com.netflixclone.backend.repository.UserRepo;

@Service
public class UserService {
    private final UserRepo userRepo;

    public UserService(UserRepo userRepo) {
        this.userRepo = userRepo;
    }

    public Optional<User> getUserById(Long id) {
        return userRepo.findById(id);
    }

    public User saveUser(User user) {
        return userRepo.save(user); 
    }

    public void deleteUser(Long id) {
        userRepo.deleteById(id);
    }

    public List<User> getAllUsers() {
        return userRepo.findAll();
    }

    public Optional<User> updatePassword(Long userId, String newPassword) {
        return userRepo.findById(userId).map(user -> {
            user.setPwd(newPassword);
            return userRepo.save(user);
        });
    }
}
