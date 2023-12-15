import pandas as pd
import mysql.connector
import warnings
warnings.filterwarnings('ignore')


class DataBasHelper:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',user='root',password='',database='campusx')
        self.mycursor = self.connection.cursor()



    def register_database(self, id, name, email, password):

        sql_query = (" insert into users values (%s, %s, %s, %s) ")
        values = (id, name, email, password)

        try:
            self.mycursor.execute(sql_query, values)
            self.connection.commit()
        except:
            print("Resister Status(DB):  Unsuccessfull")
            return -1
        else:
            print("Resister Status(DB) :  Successfull")
            return 1



    def login_database(self, email, password):

        query = ("select * from users where email like %s and password like %s")
        values = (email, password)

        try:
            self.mycursor.execute(query, values)
            data = self.mycursor.fetchall()
        except:
            print("Some error occured")
        else:
            print("run successfully")

        return data
        

    def show_database(self):
        query = ("select * from users")
        data = pd.read_sql_query(query, self.connection)
        print(data)


if __name__=='__main__':
    datamite = DataBasHelper()
    datamite.show_database()