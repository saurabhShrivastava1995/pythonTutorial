
class Library:

    def __init__(self):
        self.books = 'books.txt'

    def add_new_book(self, book_name,book_author,read_flag,mode='a'):
        with open(self.books,mode) as file:
            file.write(f'{book_name},{book_author},{read_flag}\n')

    def delete_a_book(self, book_name):
        with open(self.books, 'r+') as file:
            books_list = [line.strip().split(",") for line in file.readlines()]
            books_list = [book for book in books_list if book[0] != book_name]
            for book in books_list:
                self.add_new_book(book[0], book[1], book[2],'w')


    def find_a_book(self, book_name):
        with open(self.books, 'r') as file:
            books_list = [line.strip().split(',') for line in file.readline()]
            for book in books_list:
                if book[0] == book_name:
                    print(book)
                    break
            else:
                print("Oops!! No books found with the given name in the library")

    def mark_book_as_read(self, book_name):
        with open(self.books, 'r') as file:
            books_list = [line.strip().split(',') for line in file.readline()]
            for book in books_list:
                if book[0] == book_name:
                    self.delete_a_book(book[0])
                    self.add_new_book(book[0], book[1], bool('True'))
                    break
            else:
                print("Oops!! No books found with the given name in the library")



