import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

def find_item_name():
	soup = BeautifulSoup(ITEM_HTML,'html.parser')
	locator = 'article.product_pod h3 a'
	html_link = soup.select_one(locator)
	print(html_link.attrs.get('title'))

def find_item_price():
	soup = BeautifulSoup(ITEM_HTML,'html.parser')
	locator = 'article.product_pod div.product_price p'
	item_price = soup.select_one(locator).string
	pattern = '£([0-9]+\.[0-9]+)'
	mathcer = re.match(pattern, item_price)
	print(float(mathcer.group(1)))

def find_item_rating():
	soup = BeautifulSoup(ITEM_HTML, 'html.parser')
	locator = 'article.product_pod p'
	item_rating = soup.select_one(locator)
	arr = [x for x in item_rating.attrs['class'] if x != 'star-rating']
	print(arr[0])

find_item_name()
find_item_price()
find_item_rating()