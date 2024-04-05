import mysql.connector


class CheckInDatabase:
    def __init__(self, email, password, tableName) -> None:
        self.email = email
        self.password = password
        self.tableName = tableName

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # server host
                user="root",  # username
                password="",  # password
                database="python",  # name of database
            )
        except:
            print("DataBase not coonected")
        self.cursor = self.connection.cursor()

    # checking email and password in database
    def check(self):
        sql = f"select * from {self.tableName} where email='{self.email}' and password='{self.password}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data


# student data insertion
class StudentInsert:
    def __init__(self, enrollment, email, name, phone, address, department) -> None:
        self.enrollment = enrollment
        self.email = email
        self.name = name
        self.phone = phone
        self.address = address
        self.department = department

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # server host
                user="root",  # username
                password="",  # password
                database="python",  # name of database
            )
        except:
            print("Database not connected")
        self.cursor = self.connection.cursor()

    def check(self):
        sql = f"SELECT * FROM student WHERE enrollment = {self.enrollment}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def insert_into_database(self):
        sql = f"INSERT INTO student(enrollment, name, email, password, phone, address, department) VALUES ({self.enrollment}, '{self.name}', '{self.email}', '1234', '{self.phone}', '{self.address}', '{self.department}')"
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()


# faculty data insertion
class FacultyInsert:
    def __init__(
        self,
        email,
        name,
        phone,
        department,
        address,
        designation,
        course,
        attached_year,
    ) -> None:
        self.email = email
        self.name = name
        self.phone = phone
        self.department = department
        self.address = address
        self.designation = designation
        self.course = course
        self.attached_year = attached_year

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # server host
                user="root",  # username
                password="",  # password
                database="python",  # name of database
            )
        except:
            print("Database not connected")
        self.cursor = self.connection.cursor()

    def check(self):
        sql = f"SELECT * FROM faculty WHERE email = '{self.email}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def insert_into_database(self):
        sql = f"INSERT INTO faculty(email, name, phone, department, address, designation, course, attached_year, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            self.email,
            self.name,
            self.phone,
            self.department.upper(),
            self.address,
            self.designation.upper(),
            self.course.upper(),
            self.attached_year,
            "1234",
        )
        self.cursor.execute(sql, values)
        self.connection.commit()
