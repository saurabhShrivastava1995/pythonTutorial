import re
from locator.bookLocation import bookLocation

class BookParser:

	def __init__(self, parent):
		self.parent = parent

	def name(self):
		locator = bookLocation.NAME
		book = self.parent.select_one(locator)
		return book.attrs.get('title')

	def link(self):
		locator = bookLocation.LINK
		link = self.parent.select_one(locator)
		return link.attrs.get('href')

	def price(self):
		locator = bookLocation.PRICE
		price = self.parent.select_one(locator)
		pattern = '£([0-9]+\.[0.9]+)'
		matcher = re.match(pattern, price) 
		return mtcher.group(1)

	def rating(self):
		locator = bookLocation.RATING
		item_rating = self.parent.select_one(locator)
		arr = [x for x in item_rating.attrs['class'] if x != 'star-rating']
		return (arr[0])

