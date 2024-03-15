-- script that creates the database hbtn_0d_usa
--	and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
USE htbn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256), state_id INTEGER NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));
