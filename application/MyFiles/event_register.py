import mysql.connector


class Event:
    def __init__(self, enrollment, name, email, phone) -> None:
        self.enrollment = enrollment
        self.name = name
        self.email = email
        self.phone = phone

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

    def check_student(self):
        sql = f"SELECT * FROM student WHERE enrollment = {self.enrollment}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def check_event(self):
        sql = f"SELECT * FROM event WHERE enrollment = '{self.enrollment}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def enter_data(self):
        sql = f"insert into event(name, email, enrollment, phone) values('{self.name}', '{self.email}', '{self.enrollment}','{self.phone}')"
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
