/*
    Title: whatabook.creation
    Author: Jeff Pilcher
    Date: 02.17.2023
    Description:  WhatABook user and tables.
*/


DROP USER IF EXISTS "whatabook_user"@"localhost";
-- Create user
CREATE USER "whatabook_user"@"localhost" IDENTIFIED WITH mysql_native_password BY "MySQL8IsGreat!";

-- Apply privileges to user for database
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- Drop for duplicate protection
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

-- Store table creation
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

-- Book table creation
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

-- User table creation
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

-- Wishlist table creation
CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

-- Insert a store location 
Insert into store(store_id, locale) 
VALUES(1, '15273 SW 94th Circle, Lake Butler, FLorida, 32054');

-- Insert books
INSERT INTO book (book_name, details, author) 
VALUES('Pet Semetary', 'Horror', 'Steven King');

INSERT INTO book (book_name, details, author) 
VALUES('Christine', 'Horror', 'Steven King');

INSERT INTO book (book_name, details, author) 
VALUES('Thinner', 'Horror', 'Steven King');

INSERT INTO book (book_name, details, author) 
VALUES('Pet Semetary 2', 'Horror', 'Steven King');

INSERT INTO book (book_name, details, author) 
VALUES('The Green Mile', 'Fiction', 'Steven King');

INSERT INTO book (book_name, details, author) 
VALUES('Going Home', 'Fiction', 'A American');

INSERT INTO book (book_name, details, author) 
VALUES('Surviving Home', 'Fiction', 'A American');

INSERT INTO book (book_name, details, author) 
VALUES('Escaping Home', 'Fiction', 'A American');

INSERT INTO book (book_name, details, author) 
VALUES('Forsaking Home', 'Fiction', 'A American');

-- Insert user
INSERT INTO user (first_name, last_name) 
VALUES('Jeff', 'Pilcher');

INSERT INTO user (first_name, last_name) 
VALUES('Jeremy', 'Pilcher');

INSERT INTO user (first_name, last_name) 
VALUES('John', 'Pilcher');

-- Insert  wishlist 

INSERT INTO wishlist (user_id, book_id) 
VALUES('1', '5');

INSERT INTO wishlist (user_id, book_id) 
VALUES('2', '7');

INSERT INTO wishlist (user_id, book_id) 
VALUES('3', '3');