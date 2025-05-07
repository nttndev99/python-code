# SQLite code snippet 
# Using Cursor to create a table and insert data into it
import sqlite3

db = sqlite3.connect("./app/instance/blog.db")

cursor = db.cursor()

##------ INSERT DATA -----
data = [
    (1,
    'The Life of Cactus',
    'Who knew that cacti lived such interesting lives.',
    'Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.' 
    ),
    (2,
    'Top 15 Things to do When You are Bored',
    'Are you bored? Don\'t know what to do? Try these top 15 activities.',
    'Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.'
    ),
    (3,
    'Introduction to Intermittent Fasting',
    'Learn about the newest health craze.',
    'Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.'
    )
]
cursor.executemany("INSERT INTO posts(id, title, subtitle, body) VALUES(?, ?, ?, ?)", data)
db.commit()

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
