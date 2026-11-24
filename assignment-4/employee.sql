CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT,
    email VARCHAR(100)
);

INSERT INTO employee VALUES
(1, 'Agam', 'IT', 52000, 'agam@gmail.com'),
(2, 'Vaishnavi', 'HR', 47000, 'vaishnavi@gmail.com'),
(3, 'Vedant', 'Finance', 58000, 'vedant@gmail.com'),
(4, 'Tanisha', 'IT', 61000, 'tanisha@gmail.com'),
(5, 'Ayush', 'Sales', 43000, 'ayush@gmail.com');

SELECT * FROM employee;
