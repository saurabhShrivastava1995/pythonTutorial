import requests

from pages.page_locator import Books


page_content = requests.get("http://books.toscrape.com").content

books = Books(page_content)
for book in books.books():
	print(book.name())

