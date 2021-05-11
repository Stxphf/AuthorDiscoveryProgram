import mysql.connector
import numpy as np
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql4.freemysqlhosting.net',
                                             database='sql4407415',
                                             user='sql4407415',
                                             password='KUGU7i48WW')
    if connection.is_connected():
        books_found=[]
        cursor = connection.cursor()
        def discovery(x,y,z):
            sql_select_Query = "select * from User_Likes_Genres"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()
            user_match=[]
            
            
            for row in record:
                genre_id =str(row[0])
                user_id =str(row[1])
                if x == genre_id:
                    user_match.append(row[1])

            sql_select_Query = "select * from User_History ORDER BY user_id Asc"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()
            user_match_book=[]

            for row in record:
                user_id =(row[1])
                book_id =(row[2])
                for i in user_match:
                    if user_id == i:                        
                        user_match_book.append(row[2])

            
                        

            sql_select_Query = "select * from Books ORDER BY book_id Desc"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()
            user_match_book_score=user_match_book

            for row in record:
                book_id =(row[0])
                score =(row[3])
                user_match_book_score = np.where(user_match_book_score == book_id, score, user_match_book_score)

            
            
            user_match_book_score= np.add.reduceat(user_match_book_score, np.arange(0, len(user_match_book_score), 3))

            user_match = [user_match for _,user_match in sorted(zip(user_match_book_score,user_match))]
            user_match_book_score= sorted (user_match_book_score)

            user_match=user_match[-3:]

            sql_select_Query = "select * from User_History ORDER BY user_id Asc"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()
            user_match_book=[]

            for row in record:
                user_id =int(row[1])
                book_id =int(row[2])
                for i in user_match:
                    if user_id == i:                        
                        user_match_book.append(row[2])
            

            final_match_book=sorted(user_match_book)
            final_book_genre=[]
            
            sql_select_Query = "select * from Categorised_By"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()

            for row in record:
                book_id =(row[0])
                genre_id =(row[1])
                
                for i in final_match_book:
                    if book_id == i:                        
                        final_book_genre.append(row[1])

            z=int(z)

            sql_select_Query = "select * from Language_Written"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()

                                  
                        
            
            


            unique = set()
            duplicate=[]
            for n in final_match_book:
              if n in unique:
                duplicate.append(n)                
                final_book_genre.pop(0)

                
              else:
                unique.add(n)
                final_book_genre.pop(0)


            medium_match = [element for element in final_match_book if element not in duplicate]


            sql_select_Query = "select * from Books ORDER BY average_rating Desc"
            cursor.execute(sql_select_Query)
            record= cursor.fetchall()

            for row in record:
                book_id =int(row[0])
                for i in duplicate:
                    if book_id== i:                    
                        print(row[1], ",", row[3], ",", row[4], ",")

            for row in record:
                book_id =int(row[0])
                for i in medium_match:
                    if book_id== i:                     
                        print(row[1], ",", row[3], ",", row[4], ",")

            return(duplicate)
                  
        #genre,age,language           
        discovery("4","2","2")
        
        
except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
