import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql4.freemysqlhosting.net',
                                             database='sql4407415',
                                             user='sql4407415',
                                             password='KUGU7i48WW')
    if connection.is_connected():
        cursor = connection.cursor()
        sql_select_Query = "select * from Users"
        cursor.execute(sql_select_Query)
        record= cursor.fetchall()
        for row in record:
            print(row[3], ",",row[4], ",")
                
        
except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()