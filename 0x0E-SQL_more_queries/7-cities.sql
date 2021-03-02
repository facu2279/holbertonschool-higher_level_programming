-- Create by Facundo Diaz to Holberton School 2021

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, state_id INT NOT NULL, PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states(id))