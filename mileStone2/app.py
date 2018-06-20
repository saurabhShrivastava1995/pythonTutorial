
from utils.database import Library

lib = Library()

USER_CHOICE = """
Enter your choice:
1. Add a new book
2. Delete a book
3. Find a book
4. Mark a book as read
5. Quit

"""
res = input(USER_CHOICE)
while res != '5':
    if res == '1':
        inp = (input("Enter the book name, it's author and the read status respectively : ")).split()
        lib.add_new_book(inp[0], inp[1], bool(inp[2]))

    elif res == '2':
        inp = input('Enter the book name you want to delete : ')
        lib.delete_a_book(inp)

    elif res == '3':
        inp = input('Enter the book name you want to find : ')
        lib.find_a_book(inp)

    elif res == '4':
        inp = input('Enter the book name you want to mark as Read : ')
        lib.mark_book_as_read(inp)

    else:
        print("Exiting...")
        break
    res = input(USER_CHOICE)
