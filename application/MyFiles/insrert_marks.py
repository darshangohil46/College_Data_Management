import mysql.connector

"""
sem1 - maths1, physics, java1, software
sem2 - maths2, fee, java2, ds, dbms
sem3 - fsd, python1, de, ps, etc
sem4 - fsd2, python2, toc, dm
sem5 - daa, os, cn, coa
"""


class InsertMarks:
    def __init__(self, enrollment, subject, marks) -> None:
        self.enrollment = enrollment
        self.subject = subject
        self.marks = marks

        try:
            self.connection = mysql.connector.connect(
                host="localhost",  # server host
                user="root",  # username
                password="",  # password
                database="python",  # name of database
            )
        except:
            print("Error connecting to MySQL")

        self.cursor = self.connection.cursor()

    def check(self):
        sql = f"SELECT * FROM student WHERE enrollment = {self.enrollment}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def enter_marks(self):
        sql = f"update student set `{self.subject}`={self.marks} where enrollment={self.enrollment}"
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
