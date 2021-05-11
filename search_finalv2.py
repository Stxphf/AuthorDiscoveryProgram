import mysql.connector
from mysql.connector import Error
Books_found=[]

try:
        connection = mysql.connector.connect(host='sql4.freemysqlhosting.net',
                                             database='sql4407415',
                                             user='sql4407415',
                                             password='KUGU7i48WW')
        if connection.is_connected():
            cursor = connection.cursor()
            def Search(x):

                sql_select_Query = "select * from Books"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()
                if len(x) == 10 or len(x) == 13 and x.isdigit():
                        isbn_search=False
                        for row in record:                    
                            isbn=str(row[4])
                            publisher_id=(row[5])                    
                            if x == isbn:                            
                                isbn_search=True
                        print(isbn_search)
                        if isbn_search == False:
                                return False
                        
                sql_select_Query = "select * from Authors"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()
                author_id_found=[]
                for row in record:
                    author_id=(row[0])
                    author_name=(row[1])                
                    if x in author_name:
                        author_id_found.append(row[0])
                

                        
                sql_select_Query = "select * from Written_By"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()
                for row in record:
                    book_id=(row[0])
                    author_id=(row[1])
                    for i in author_id_found:
                        if i == author_id:
                            Books_found.append(row[0])

                sql_select_Query = "select * from Publishers"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()
                publisher_id_found=[]
                for row in record:
                    publisher_id=(row[0])
                    publisher=(row[1])
                    if x in publisher:
                        publisher_id_found.append(row[0])

                sql_select_Query = "select * from Genres"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()
                genre_id_found=[]
                for row in record:
                    genre_id=(row[0])
                    genre=(row[1])
                    if x in genre:
                        genre_id_found.append(row[0])
                


                sql_select_Query = "select * from Categorised_By"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()                
                for row in record:
                    book_id=(row[0])
                    genre_id=(row[1])
                    for i in genre_id_found:
                        if i == genre_id:
                            Books_found.append(row[0])


                sql_select_Query = "select * from Books"
                cursor.execute(sql_select_Query)
                record= cursor.fetchall()                
                for row in record:
                    book_id=(row[0])
                    title=(row[1])
                    age_rating_id=(row[2])
                    average_rating=(row[3])
                    isbn=str(row[4])
                    publisher_id=(row[5])
                    if x in title:
                        Books_found.append(row[0])
                    if x in isbn:
                        Books_found.append(row[0])
                    for i in publisher_id_found:
                        if i ==publisher_id:
                            Books_found.append(row[0])
                    
                    


                
                        
                        
            #user inputs checks if its and isbn and if its isbn does it contain in our database        
            if Search("Mortimer") == False:
                    print("please enter book")
            else:    
                    sql_select_Query = "select * from Books ORDER BY average_rating Desc"
                    cursor.execute(sql_select_Query)
                    record= cursor.fetchall()                
                    for row in record:
                        book_id=(row[0])
                        title=(row[1])
                        age_rating_id=(row[2])
                        average_rating=(row[3])
                        isbn=str(row[4])
                        publisher_id=(row[5])
                        for i in Books_found:
                            if i == book_id:
                                print("ID ",book_id,"title ",title,"age ",age_rating_id,"score ",average_rating,"isbn",isbn,"publisher",publisher_id)
            print("no more books found")
                
            

except Error as e:
        print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
