CREATE TABLE plats (
 id INT PRIMARY KEY,
 nom VARCHAR(100),
 prix DECIMAL(10,2)
);

CREATE TABLE clients (
 id INT PRIMARY KEY,
 nom VARCHAR(100),
 telephone VARCHAR(20)
);

CREATE TABLE commandes (
 id INT PRIMARY KEY,
 client_id INT,
 plat_id INT
);