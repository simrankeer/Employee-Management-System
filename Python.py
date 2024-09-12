#PYTHON CODE USED IN THIS PROJECT
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
