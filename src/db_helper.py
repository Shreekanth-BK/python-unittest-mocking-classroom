import mysql.connector


class DbHelper:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user='root',
            password='ssit',
            database="emp",
            auth_plugin='mysql_native_password'
            )
        self.mycursor = self.mydb.cursor()

    def get_maximum_salary(self):
        self.mycursor.execute("select max(salary) from employee;")
        myresult = self.mycursor.fetchall()
        return myresult[0][0]

    def get_minimum_salary(self):
        self.mycursor.execute("select min(salary) from employee;")
        myresult = self.mycursor.fetchall()
        return myresult[0][0]

if __name__ == "__main__":
    db_helper = DbHelper()
    max_salary = db_helper.get_maximum_salary()
    min_salary = db_helper.get_minimum_salary()
    print(max_salary)
    print(min_salary)