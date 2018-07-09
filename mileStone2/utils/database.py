import sqlite3
from utils.database_connections import DatabaseConnection

class Library:

    def create_book_table(self):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text,read integer)')

    def add_new_book(self, book_name, book_author, read_flag):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            if read_flag == 'True':
                cursor.execute('INSERT INTO books VALUES(?,?,0)',(book_name,book_author))
            else:
                cursor.execute('INSERT INTO books VALUES(?,?,1)',(book_name,book_author))


    def delete_a_book(self, book_name):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM books WHERE name=?',(book_name,))


    def find_a_book(self, book_name):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM books WHERE name=?',(book_name,))
            print(cursor.fetchall())

        

    def mark_book_as_read(self, book_name):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE books SET read=0 WHERE name=?',(book_name,))
        
