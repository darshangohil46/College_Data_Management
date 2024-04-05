import mysql.connector


# remove student from database
class Remove_student:
    def __init__(self, email, enrollment) -> None:
        self.email = email
        self.enrollment = enrollment

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # server host
                user="root",  # username
                password="",  # password
                database="python",  # name of database
            )
        except mysql.connector.Error as e:
            print("Error connecting to MySQL")

        self.cursor = self.connection.cursor()

    def check(self):
        print(self.enrollment)
        sql = f"SELECT * FROM student WHERE enrollment={self.enrollment} and email='{self.email}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def remove_student(self):
        sql = f"DELETE FROM student WHERE email = '{self.email}' AND enrollment = {self.enrollment}"
        self.cursor.execute(sql)
        self.connection.commit()


class Remove_faculty:
    def __init__(self, email, id) -> None:
        self.email = email
        self.id = id

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # server host
                user="root",  # username
                password="",  # password
                database="python",  # name of database
            )
        except mysql.connector.Error as e:
            print("Error connecting to MySQL")

        self.cursor = self.connection.cursor()

    def check(self):
        sql = f"SELECT * FROM faculty WHERE email = '{self.email}' AND id = {self.id}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def remove_faculty(self):
        sql = f"DELETE FROM faculty WHERE email = '{self.email}' AND id = {self.id}"
        self.cursor.execute(sql)
        self.connection.commit()
