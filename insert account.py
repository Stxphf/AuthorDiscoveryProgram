import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql4.freemysqlhosting.net',
                                             database='sql4407415',
                                             user='sql4407415',
                                             password='KUGU7i48WW')
    if connection.is_connected():
        cursor = connection.cursor()
        def insert_account(userfn,userln,usere,userp,userDOB,age_rating_id,language,genre,book1,book2,book3):
            
            #user_no=cursor.lastrowid
            
            add_user=("""INSERT INTO Users
                      (user_first_name, user_last_name, user_email,user_password,user_DOB,age_rating_id,language_id)
                      VALUES(%s,%s,%s,%s,%s,
                      (SELECT age_rating_id from Age_Ratings WHERE age_rating = %s),
                      (SELECT language_id from Languages WHERE language = %s))""")
                      
                      
            data_user=(userfn,userln,usere,userp,userDOB,age_rating_id,language)
            cursor.execute(add_user,data_user)

            connection.commit()
            
            user = cursor.lastrowid
            print(user)
            
            
            add_book=("""INSERT INTO User_History
                        (user_id,book_id)
                        Values(%s,(Select book_id from Books WHERE book_id=%s))""")
            
            data_user=(user,book1)
            cursor.execute(add_book,data_user)
            data_user=(user,book2)
            cursor.execute(add_book,data_user)
            data_user=(user,book3)
            cursor.execute(add_book,data_user)
            connection.commit()

            add_genre=("""INSERT INTO User_Likes_Genres
                            (user_id,genre_id)
                            Values(%s,(Select genre_id from Genres WHERE genre=%s))""")
            
            data_user=(user,genre)
            cursor.execute(add_genre,data_user)
            connection.commit()
            
                
            
            

#inputs are firstname lastname email password DOB age rating language genre like and 3 book recomends
        insert_account("zsolt","bolla","user@gmail.com","password","20001112","4","english","History","14","18","20")
except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        
        connection.close()
        print("MySQL connection is closed")
