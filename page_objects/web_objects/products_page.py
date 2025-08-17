from playwright.sync_api import Page
import allure

from extentions.ui_actions import UiActions


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.product = None
        self.page_header = self.page.locator("[class='brand greenLogo']")
        self.search_box = self.page.locator("input[type='search']")
        self.no_results_large_message = self.page.locator("[class='no-results'] h2")
        self.no_results_small_message = self.page.locator("[class='no-results'] p")
        self.no_results_image = self.page.locator("[class='no-results'] img")
        self.items_indicator_header = self.page.locator("[class='cart-info'] tr:first-child strong")
        self.price_indicator_header = self.page.locator("[class='cart-info'] tr:last-child strong")
        self.cart_icon = self.page.locator("[class='cart-icon']")
        self.product_name_in_cart = self.page.locator("p[class='product-name']")
        self.product_original_price_in_cart = self.page.locator("[class='cart-item'] p[class='product-price']")
        self.product_total_amount_in_cart = self.page.locator("p[class='amount']")
        self.quantity = self.page.locator("[class='cart-item'] [class='quantity']")
        self.proceed_to_checkout = self.page.locator("text=PROCEED TO CHECKOUT")

    def get_search_box(self):
        return self.search_box

    def get_no_results(self):
        return self.no_results_large_message

    def get_no_results_small(self):
        return self.no_results_small_message

    def get_no_results_image(self):
        return self.no_results_image

    def locate_product(self, product_name):
        self.product = self.page.locator(f"//*[contains(text(), '{product_name}')]")

    def add_to_cart_button(self):
        return self.product.locator("//../div[3]/button")

    def get_price_product(self):
        return self.product.locator("//../p").nth(2)
        
    def get_page_header_text(self):
        return self.page_header.text_content()

    def increment_action_decrease(self):
        return self.product.locator("//../div[2]/a[1]")

    def increment_action_increase(self):
        return self.product.locator("//../div[2]/a[2]")

    def get_items_indicator_header(self):
        return self.items_indicator_header

    def get_price_indicator_header(self):
        return self.price_indicator_header

    def get_product_name_in_cart(self):
        return self.product_name_in_cart

    def get_product_original_price_in_cart(self):
        return self.product_original_price_in_cart

    def get_product_total_amount_in_cart(self):
        return self.product_total_amount_in_cart

    def get_cart_icon(self):
        return self.cart_icon

    def get_quantity(self):
        return self.quantity

    def get_proceed_to_checkout(self):
        return self.proceed_to_checkout

    # def increment_product_one_click(self, product_name):
    #     product_price = self.get_price_one_product(product_name)
    #     UiActions.click(
    #         self.product.locator("//../div[2]/a[2]"))
    #     product_price = product_price * 2
    #     return product_price
    #
    # def increment_product_two_click(self, product_name):
    #     product_price = self.get_price_three_products(product_name)
    #     UiActions.double_click(
    #         self.product.locator("//../div[2]/a[2]"))
    #     product_price = product_price * 3
    #     return product_price

    # @allure.step("Get price of one product")
    # def get_price_one_product(self, product_name):
    #     for product in self.products:
    #         if product['name'] == product_name:
    #             return product['price']
    #
    # @allure.step("Get price of two product")
    # def get_price_one_product(self, product_name):
    #     for product in self.products:
    #         if product['name'] == product_name:
    #             return product['price_two_products'], product['price_after_3_products']

    # @allure.step("Get price of three product")
    # @allure.step("Fill search box with text")
    # def get_price_three_products(self, product_name):
    #     for product in self.products:
    #         if product['name'] == product_name:
    #             return product['price_after_3_products']

    @allure.step("Fill search box with text")
    def fill_search_box(self, text):
        self.search_box.fill(text)

    @allure.step("Proceed to checkout page")
    def proceed_to_checkout_flow(self):
        UiActions.click(self.get_cart_icon())
        UiActions.click(self.get_proceed_to_checkout())
