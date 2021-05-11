import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql4.freemysqlhosting.net',
                                             database='sql4407415',
                                             user='sql4407415',
                                             password='KUGU7i48WW')
    if connection.is_connected():
        cursor = connection.cursor()
        def insert_book(title,age,score,isbn,publisher,author,genre,lang):
            sql_select_Query = "select * from Publishers"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()
            publisher_search=False
            for row in record:
                publisher_id=str(row[0])
                publisher_check=row[1]
                if publisher == publisher_check:
                    publisher_search=True
            print("test,")       
            if publisher_search == False:
                add_publisher=("""INSERT INTO Publishers
                                (publisher)
                                VALUES(%s)""")
                
                cursor.execute(add_publisher,(publisher,))
                print("publisher")
                connection.commit()



                
            #add_book("""INSERT INTO Books
                        #(title,age_rating_id,average_rating,isbn,publisher_id)
                        #VALUES(%s,
                        #(SELECT age_rating_id from Age_Ratings WHERE age_rating = %s),%s,%s
                        #(SELECT publisher_id from Publishers WHERE publisher = %s))""")
            
        #inputs title, age rating id,score, isbn, publisher name, author name , genre, language
        insert_book("I Like turtles","2","4","1234567890","Steve books", "Steve","History","english")
except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        
        connection.close()
        print("MySQL connection is closed")
