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

Setup and Installation
Clone the Repository:
git clone https://github.com/your-simrankeer/employee-management-system.git

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

Run the Application: Execute the Python script to start the application:
file:///C:/Users/Harsh/Downloads/Employee%20Management%20System%20(1).pdf
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="employee_management_system"
    )
    cursor = con.cursor()
except mysql.connector.Error as err:
    print(f"Error: Could not connect to database: {err}")
    exit(1)
    
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor.execute(sql, (employee_id,))
    # Fetch the result before running any other query
    result = cursor.fetchall()
    return len(result) > 0

def add_employee():
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return
    
    Name = input("Enter Employee Name: ")
    Post = input("Enter Employee Post: ")
    
    try:
        Salary = float(input("Enter Employee Salary: "))
    except ValueError:
        print("Invalid Salary! Please enter a valid number.")
        return

    sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
    data = (Id, Name, Post, Salary)
    
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

def remove_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    sql = 'DELETE FROM employees WHERE id=%s'
    data = (Id,)
    
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Removed Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

def promote_employee():
    Id = input("Enter Employee's Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    try:
        Amount = float(input("Enter increase in Salary: "))
        sql_select = 'SELECT salary FROM employees WHERE id=%s'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount

        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        print("Employee Promoted Successfully")

    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()

def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    try:
        menu()
    finally:
        cursor.close()
        con.close()

Upon running the application, you will be presented with a menu to perform various operations:
Add Employee: Follow the prompts to enter employee details.
Remove Employee: Enter the ID of the employee you wish to remove.
Promote Employee: Enter the ID of the employee and the amount to increase their salary.
Display Employees: View details of all employees.

Error Handling
The application includes basic error handling to manage issues such as invalid input and database connection errors. If an error occurs, appropriate messages are displayed, and transactions are rolled back if needed.
