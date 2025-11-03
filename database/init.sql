USE master
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'netflix_clone')
	DROP DATABASE netflix_clone
GO

CREATE DATABASE netflix_clone
GO

USE netflix_clone
GO

SET DATEFIRST 7
GO



IF OBJECT_ID('[dbo].[user]', 'U') IS NOT NULL
    DROP TABLE [dbo].[user];

CREATE TABLE [dbo].[user] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email NVARCHAR(255) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    name NVARCHAR(255) NOT NULL,
    gender NVARCHAR(50) NOT NULL CHECK (type IN ('male', 'female')),
    dob DATE NOT NULL,

    CONSTRAINT [User email format is invalid] CHECK (email LIKE '%_@__%.__%'),
    CONSTRAINT [A user with this email already exists] UNIQUE (email),
    CONSTRAINT [User password must be at least 8 characters long] CHECK (LEN(password) >= 8),
    CONSTRAINT [User must be at least 13 years old] CHECK (DATEDIFF(YEAR, dob, GETDATE()) >= 13)
);
GO

IF OBJECT_ID('[dbo].[movie]', 'U') IS NOT NULL
    DROP TABLE [dbo].[movie];

CREATE TABLE [dbo].[movie] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX) NOT NULL,
    release_date DATE NOT NULL,
    raterCount INT DEFAULT 0,
    rating DECIMAL(3, 1),
    poster_url NVARCHAR(2083),
    price DECIMAL(10, 2) NOT NULL,
    duration INT NOT NULL,

    CONSTRAINT [Movie title must be unique] UNIQUE (title),
    CONSTRAINT [Movie rating must be between 0 and 5] CHECK (rating >= 0 AND rating <= 5),
    CONSTRAINT [Movie release date cannot be in the future] CHECK (release_date <= GETDATE()),
    CONSTRAINT [Movie rater count must be non-negative] CHECK (raterCount >= 0),
    CONSTRAINT [Movie price must be non-negative] CHECK (price >= 0),
    CONSTRAINT [Movie duration must be positive] CHECK (duration > 0),
    CONSTRAINT [Movie poster URL format is invalid] CHECK (poster_url IS NULL OR poster_url LIKE 'http%'),

);
GO

IF OBJECT_ID('[dbo].[genre]', 'U') IS NOT NULL
    DROP TABLE [dbo].[genre];

CREATE TABLE [dbo].[genre] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL UNIQUE,
);

IF OBJECT_ID('[dbo].[movie_genre]', 'U') IS NOT NULL
    DROP TABLE [dbo].[movie_genre];

CREATE TABLE [dbo].[movie_genre] (
    movie_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (movie_id, genre_id),

    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES [dbo].[genre](id) ON DELETE CASCADE
);

IF OBJECT_ID('[dbo].[Media]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Media];

CREATE TABLE [dbo].[Media] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    movie_id INT NOT NULL,
    type NVARCHAR(50) NOT NULL CHECK (type IN ('trailer', 'video')),
    url NVARCHAR(2083) NOT NULL,

    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES [dbo].[user](id) ON DELETE CASCADE,
    CONSTRAINT [Media URL format is invalid] CHECK (url LIKE 'http%')
);

IF OBJECT_ID('[dbo].[watch_progress]', 'U') IS NOT NULL
    DROP TABLE [dbo].[watch_progress];

CREATE TABLE [dbo].[watch_progress] (
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    progress INT NOT NULL CHECK (progress >= 0),
    PRIMARY KEY (user_id, movie_id),

    FOREIGN KEY (user_id) REFERENCES [dbo].[user](id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE
);
GO

IF OBJECT_ID('[dbo].[owned_movie]', 'U') IS NOT NULL
    DROP TABLE [dbo].[owned_movie];

CREATE TABLE [dbo].[owned_movie] (
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    PRIMARY KEY (user_id, movie_id),

    FOREIGN KEY (user_id) REFERENCES [dbo].[user](id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE
);
GO

IF OBJECT_ID('[dbo].[review]', 'U') IS NOT NULL
    DROP TABLE [dbo].[review];

CREATE TABLE [dbo].[review] (
    created_at DATETIME DEFAULT GETDATE(),
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    rating DECIMAL(3, 1) CHECK (rating >= 0 AND rating <= 5),
    comment NVARCHAR(MAX) NOT NULL,

    PRIMARY KEY (created_at, user_id, movie_id),

    FOREIGN KEY (user_id) REFERENCES [dbo].[user](id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE
);
GO

IF OBJECT_ID('[dbo].[person]', 'U') IS NOT NULL
    DROP TABLE [dbo].[person];

CREATE TABLE [dbo].[person] (
    id INT IDENTITY(1,1) PRIMARY KEY,   
    name NVARCHAR(255) NOT NULL,
    biography NVARCHAR(MAX) NOT NULL,
    dob DATE NOT NULL,
    photo_url NVARCHAR(2083) NOT NULL check (photo_url LIKE 'http%'),
    gender NVARCHAR(50) NOT NULL CHECK (gender IN ('male', 'female'))
);


IF OBJECT_ID('[dbo].[movie_person]', 'U') IS NOT NULL
    DROP TABLE [dbo].[movie_person];

CREATE TABLE [dbo].[movie_person] (
    movie_id INT NOT NULL,
    person_id INT NOT NULL,
    role NVARCHAR(50) NOT NULL CHECK (role IN ('actor', 'director', 'producer')),
    PRIMARY KEY (movie_id, person_id, role),

    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE,
    FOREIGN KEY (person_id) REFERENCES [dbo].[person](id) ON DELETE CASCADE
);
GO

IF OBJECT_ID('[dbo].[transaction]', 'U') IS NOT NULL
    DROP TABLE [dbo].[transaction];

CREATE TABLE [dbo].[transaction] (
    id INT IDENTITY(1,1) PRIMARY KEY,   
    user_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATETIME DEFAULT GETDATE(),
    status NVARCHAR(50) NOT NULL CHECK (status IN ('pending', 'completed', 'failed')),
    
    FOREIGN KEY (user_id) REFERENCES [dbo].[user](id) ON DELETE CASCADE,
    CONSTRAINT [Transaction amount must be positive] CHECK (amount > 0)
);
GO

CREATE TABLE [dbo].[transaction_detail] (
    transaction_id INT NOT NULL,
    movie_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (transaction_id, movie_id),

    FOREIGN KEY (transaction_id) REFERENCES [dbo].[transaction](id) ON DELETE CASCADE,  
    FOREIGN KEY (movie_id) REFERENCES [dbo].[movie](id) ON DELETE CASCADE
);

PRINT 'Database netflix_clone created successfully.'
GO

CREATE OR ALTER TRIGGER [dbo].[tg_transaction_insert_updateAmount]
ON [dbo].[transaction]
AFTER INSERT
AS
BEGIN TRANSACTION

COMMIT TRANSACTION
GO