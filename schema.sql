CREATE DATABASE IF NOT EXISTS helpdesk;
USE helpdesk;

CREATE TABLE IF NOT EXISTS teachers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(80), department VARCHAR(60), room VARCHAR(20), availability VARCHAR(60));
CREATE TABLE IF NOT EXISTS transport (id INT AUTO_INCREMENT PRIMARY KEY, route VARCHAR(80), bus_number VARCHAR(20), timing VARCHAR(40));
CREATE TABLE IF NOT EXISTS library (id INT AUTO_INCREMENT PRIMARY KEY, book_name VARCHAR(120), status VARCHAR(20));
CREATE TABLE IF NOT EXISTS labs (id INT AUTO_INCREMENT PRIMARY KEY, lab_name VARCHAR(80), room VARCHAR(20), availability VARCHAR(60));
CREATE TABLE IF NOT EXISTS canteen (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(60), price DECIMAL(6,2));

INSERT INTO teachers (name, department, room, availability) VALUES
('Dr. R. Kumar','Computer Science','SJT 301','Mon-Fri 10-12'),
('Dr. S. Priya','Chemistry','TT 204','Tue, Thu 2-4'),
('Prof. A. Ravi','Mathematics','SMV 110','Mon, Wed 11-1');
INSERT INTO transport (route, bus_number, timing) VALUES
('Katpadi - Campus','B12','7:30 AM'),('Vellore Fort - Campus','B07','8:00 AM'),('Campus - Katpadi','B12','5:30 PM');
INSERT INTO library (book_name, status) VALUES
('Python Crash Course','Available'),('Database System Concepts','Issued'),('Let Us C','Available');
INSERT INTO labs (lab_name, room, availability) VALUES
('Python Lab','SJT 512','Free after 3 PM'),('Chemistry Lab','TT 101','Booked'),('Electronics Lab','SMV 220','Free');
INSERT INTO canteen (item, price) VALUES ('Masala Dosa',50),('Veg Biryani',90),('Tea',15),('Samosa',20);
