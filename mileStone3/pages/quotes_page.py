from bs4 import BeautifulSoup
from locators.quotes_page_locators import QuotePageLocators
from parser.quote import QuoteParser

class QuotesPage:

	def __init__(self, page_content):
		self.soup = BeautifulSoup(page_content, 'html.parser')

	@property	
	def quotes(self):
		locator = QuotePageLocators.QUOTE
		quote_tags = self.soup.select(locator)
		return [QuoteParser(e) for e in quote_tags]


