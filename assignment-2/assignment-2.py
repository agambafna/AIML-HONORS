import csv
import os


class Employee:

    def __init__(self):
        self.fname = "employee.csv"
        if not os.path.exists(self.fname):
            with open(self.fname, "w", newline="") as f:
                csv.writer(f).writerow(["emp_id", "name", "department", "salary", "email"])

    def read(self):
        with open(self.fname, "r") as f:
            for row in csv.reader(f):
                print(row)

    def create(self):
        eid  = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        sal  = input("Enter Salary: ")
        mail = input("Enter Email: ")
        with open(self.fname, "a", newline="") as f:
            csv.writer(f).writerow([eid, name, dept, sal, mail])
        print("Employee added!")

    def update(self):
        eid  = input("Enter Employee ID: ")
        name = input("Enter New Name: ")
        rows = []
        with open(self.fname, "r") as f:
            for row in csv.reader(f):
                if row[0] == eid:
                    row[1] = name
                rows.append(row)
        with open(self.fname, "w", newline="") as f:
            csv.writer(f).writerows(rows)
        print("Employee updated!")

    def delete(self):
        eid = input("Enter Employee ID: ")
        rows = []
        with open(self.fname, "r") as f:
            for row in csv.reader(f):
                if row[0] != eid:
                    rows.append(row)
        with open(self.fname, "w", newline="") as f:
            csv.writer(f).writerows(rows)
        print("Employee deleted!")


emp = Employee()

while True:
    print("""
1. Create Employee
2. Read Employees
3. Update Employee
4. Delete Employee
5. Exit
""")
    choice = input("Enter choice: ")

    if choice == "1":
        emp.create()
    elif choice == "2":
        emp.read()
    elif choice == "3":
        emp.update()
    elif choice == "4":
        emp.delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
