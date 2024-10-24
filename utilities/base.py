from page_objects.web_objects.check_out_page import CheckOutPage
from page_objects.web_objects.country_page import CountryPage
from page_objects.web_objects.products_page import ProductsPage

# Playwright Objects
page = None
browser = None
context = None

# Page Objects
products_page = None

check_out_page = None
country_page = None
api_actions = None


class Base:

    @staticmethod
    def init_pages():
        globals()['products_page'] = ProductsPage(page)
        globals()['check_out_page'] = CheckOutPage(page)
        globals()['country_page'] = CountryPage(page)

    @staticmethod
    def calculate_total_price(quantity: int, price: int):
        total = quantity * price
        return total

    @staticmethod
    def split_string(text: str):
        text_split = text.split(" ")
        return int(text_split[0])
