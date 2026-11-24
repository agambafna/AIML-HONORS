import pymysql


class Employee:

    def __init__(self):
        self.db = {
            "host": "localhost",
            "user": "root",
            "password": "agam@1234",
            "database": "company_db"
        }
        con = pymysql.connect(**self.db)
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee(
                id INT PRIMARY KEY,
                name VARCHAR(100),
                department VARCHAR(100),
                salary FLOAT,
                email VARCHAR(100)
            )
        """)
        con.commit()
        cur.close()
        con.close()

    def create(self):
        try:
            con = pymysql.connect(**self.db)
            cur = con.cursor()
            eid  = input("Enter ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            sal  = input("Enter Salary: ")
            mail = input("Enter Email: ")
            cur.execute("INSERT INTO employee VALUES(%s,%s,%s,%s,%s)", (eid, name, dept, sal, mail))
            con.commit()
            print("Employee added!")
        except Exception as e:
            print("Error:", e)
        finally:
            cur.close()
            con.close()

    def read(self):
        try:
            con = pymysql.connect(**self.db)
            cur = con.cursor()
            cur.execute("SELECT * FROM employee")
            for row in cur.fetchall():
                print(row)
        except Exception as e:
            print("Error:", e)
        finally:
            cur.close()
            con.close()

    def update(self):
        try:
            con = pymysql.connect(**self.db)
            cur = con.cursor()
            eid  = input("Enter ID: ")
            name = input("Enter New Name: ")
            cur.execute("UPDATE employee SET name=%s WHERE id=%s", (name, eid))
            con.commit()
            print("Employee updated!")
        except Exception as e:
            print("Error:", e)
        finally:
            cur.close()
            con.close()

    def delete(self):
        try:
            con = pymysql.connect(**self.db)
            cur = con.cursor()
            eid = input("Enter ID: ")
            cur.execute("DELETE FROM employee WHERE id=%s", (eid,))
            con.commit()
            print("Employee deleted!")
        except Exception as e:
            print("Error:", e)
        finally:
            cur.close()
            con.close()


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
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
