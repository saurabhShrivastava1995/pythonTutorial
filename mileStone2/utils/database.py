
class Library:

    def __init__()
        books = []



    def add_new_book(book_name,book_author,read_flag):
        books.append({'name': book_name,'author':book_author,'read':read_flag})



    def delete_a_book(book_name):
        books = [book for book in books if book['name'] != book_name]



    def find_a_book(book_name):
        for book in books:
            if book['name'] == book_name:
                print(book)
                break
        else:
            print("Book not found baby!!!")



    def mark_book_as_read(book_name):
        for book in books:
            if book['name'] == book_name:
                book['read'] = True
                break
        else:
            print("No book found wiht the given name")



