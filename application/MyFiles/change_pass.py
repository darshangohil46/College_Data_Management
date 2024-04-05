import mysql.connector


class Change_pass:
    def __init__(self, current_pass, new_pass, enrollment, table) -> None:
        self.current_pass = current_pass
        self.new_pass = new_pass
        self.enrollment = enrollment
        self.table = table

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
        if self.table == "student":
            sql = f"SELECT * FROM student WHERE enrollment = {self.enrollment} and password = '{self.current_pass}' "
        elif self.table == "faculty":
            sql = f"SELECT * FROM faculty WHERE id = {self.enrollment} and password = '{self.current_pass}' "
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def change(self):
        if self.table == "student":
            sql = f"UPDATE student SET password = '{self.new_pass}' WHERE enrollment = {self.enrollment}"
        elif self.table == "faculty":
            sql = f"UPDATE faculty SET password = '{self.new_pass}' WHERE id = {self.enrollment}"

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
