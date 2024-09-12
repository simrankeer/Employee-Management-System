#Employee Management System
Overview
The Employee Management System is a command-line application designed to manage employee records using a MySQL database. 
This project allows users to perform basic CRUD (Create, Read, Update, Delete) operations on employee data. 
The system supports adding new employees, removing existing employees, promoting employees by increasing their salary, and displaying a list of all employees.

Features
Add Employee: Enter details including ID, name, position, and salary to add a new employee to the system.
Remove Employee: Remove an employee from the system based on their ID.
Promote Employee: Increase the salary of an existing employee.
Display Employees: View details of all employees currently in the database.

Technologies Used
Python: Programming language used to implement the application logic.
MySQL: Database management system for storing employee records.
mysql-connector-python: Python library used to interact with the MySQL database.

Install Dependencies: Make sure you have Python and MySQL Connector installed. You can install the MySQL Connector using pip:
pip install mysql-connector-python

Database Configuration:
Ensure MySQL Server is running.
Create a database named employee_management_system in MySQL.
Create a table employees with the following schema:

CREATE TABLE employees (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

Run python code
Upon running the code, you will be presented with a menu to perform various operations:
Add Employee: Follow the prompts to enter employee details.
Remove Employee: Enter the ID of the employee you wish to remove.
Promote Employee: Enter the ID of the employee and the amount to increase their salary.
Display Employees: View details of all employees.

Error Handling
The application includes basic error handling to manage issues such as invalid input and database connection errors. If an error occurs, appropriate messages are displayed, and transactions are rolled back if needed.
