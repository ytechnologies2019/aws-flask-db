pip install Flask Flask-SQLAlchemy mysqlclient

-- Create the database (if not already created)
CREATE DATABASE your_database;

-- Use the database
USE your_database;

-- Create the table with the name `flask-input-db` (escaped with backticks)
CREATE TABLE `flask-input-db` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

