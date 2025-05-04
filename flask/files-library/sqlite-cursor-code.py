# SQLite code snippet 
# Using Cursor to create a table and insert data into it
import sqlite3

db = sqlite3.connect("./instance/books.db")

cursor = db.cursor()

##----- CREATE TABLE-----
# table = '''
# CREATE TABLE book (
#     id INTEGER PRIMARY KEY, 
#     title varchar(250) NOT NULL UNIQUE, 
#     author varchar(250) NOT NULL, 
#     rating FLOAT NOT NULL)
# '''
# cursor.execute(drop_table)

# #----- DROP TABLE-----
# drop_table = '''
# DROP TABLE IF EXISTS book;
# '''
# cursor.execute(drop_table)



##------ INSERT DATA -----
# data = (3, 'Harry Potter3', 'J. K. Rowling', '9.3')
# cursor.execute("INSERT INTO books VALUES(?, ?, ?, ?)", data)
# db.commit()

##------ READ DATA with id-----
# id = 1
# cursor.execute("SELECT title, author FROM books WHERE id=?", (id,))
# result = cursor.fetchone()
# print(result)

##------ UPDATE DATA with id------
# id_update = 2
# cursor.execute("UPDATE books SET title = 'AAAAA' WHERE id = ?", (id_update,))
# db.commit()

##------ DELETE DATA with id------
# id_delete = 2
# sql_delete = "DELETE FROM books WHERE id = ?"
# cursor.execute(sql_delete, (id_delete,))
# db.commit()
