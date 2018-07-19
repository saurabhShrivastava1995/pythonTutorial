from bs4 import BeautifulSoup
from parser.book_parser import BookParser
from locator.booksLocationPage import BooksLocator

class Books:
	
	def __init__(self, page_content):
		self.soup = BeautifulSoup(page_content,'html.parser')
		
	def books(self):
		books = self.soup.select(BooksLocator.BOOKS)
		return [BookParser(book) for book in books]