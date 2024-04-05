import mysql.connector


class Edit_student:
    def __init__(self, enrollment, attribute, new_value) -> None:
        self.enrollment = enrollment
        self.attribute = attribute
        self.new_value = new_value

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

    def change(self):
        sql = f"UPDATE student SET {self.attribute} = '{self.new_value}' WHERE enrollment = {self.enrollment}"
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()


class Edit_faculty:
    def __init__(self, id, attribute, new_value) -> None:
        self.id = id
        self.attribute = attribute
        self.new_value = new_value

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
        sql = f"SELECT * FROM faculty WHERE id = {self.id}"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def change(self):
        sql = f"UPDATE faculty SET {self.attribute} = '{self.new_value}' WHERE id = {self.id}"
        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
