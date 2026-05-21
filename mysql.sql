CREATE DATABASE restaurant_db;

USE restaurant_db;

CREATE TABLE plats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prix FLOAT,
    categorie VARCHAR(100)
);
