
import sqlite3
class Library:

    def create_book_table(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text,read integer)')
        connection.commit()
        connection.close()

    def __init__(self):
        self.books = 'books.txt'
        self.book_list = []

    def add_new_book(self, book_name,book_author,read_flag):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        if read_flag == 'True':
            cursor.execute('INSERT INTO books VALUES(?,?,0)',(book_name,book_author))
        else:
            cursor.execute('INSERT INTO books VALUES(?,?,1)',(book_name,book_author))
        
        connection.commit()
        connection.close()


    def delete_a_book(self, book_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?',(book_name,))
        connection.commit()
        connection.close()


    def find_a_book(self, book_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE name=?',(book_name,))
        print(cursor.fetchall())
        connection.close()

        

    def mark_book_as_read(self, book_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=0 WHERE name=?',(book_name,))
        connection.commit()
        connection.close()
        
