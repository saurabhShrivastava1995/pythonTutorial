
class Library:

    def __init__(self):
        self.books = []



    def add_new_book(self, book_name,book_author,read_flag):
        self.books.append({'name': book_name,'author':book_author,'read':read_flag})



    def delete_a_book(self, book_name):
        self.books = [book for book in self.books if book['name'] != book_name]



    def find_a_book(self, book_name):
        for book in self.books:
            if book['name'] == book_name:
                print(book)
                break
        else:
            print("Book not found baby!!!")



    def mark_book_as_read(self, book_name):
        for book in self.books:
            if book['name'] == book_name:
                book['read'] = True
                break
        else:
            print("No book found with the given name")



