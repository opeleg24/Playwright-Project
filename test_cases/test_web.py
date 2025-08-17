import pytest
import allure

from utilities.common_ops import get_data

from workflows.web_flow import WebFlows


@pytest.mark.usefixtures('init_page')
class Test_Web:

    @allure.title("Test01: Verify page header text")
    @allure.description("This test verifies that the page header displays the correct text")
    def test_verify_page_header(self):
        WebFlows.verify_page_header(get_data("PAGE_HEADER"))

    @allure.title("Test02: Verify initial amount of items & products in header display")
    @allure.description("This test verifies the initial amount of items & products in the header display")
    def test_verify_initial_header_amount(self):
        WebFlows.verify_initial_amount_in_header_display(get_data("COUNTER_INITIAL"),
                                                         get_data("COUNTER_INITIAL"))

    @allure.title("Test02: Add product to cart - verify amount in header display")
    @allure.description("This test adds a product to the cart and verifies the amount in the header display")
    def test_verify_add_product_to_cart(self):
        WebFlows.add_product_to_cart(get_data("PRODUCT"))
        WebFlows.click_cart_button()
        WebFlows.verify_cart_information_in_header_display(get_data("COUNTER_ONE_PRODUCT"),
                                                           get_data("PRODUCT_ONE_PRICE"))

    @pytest.mark.usefixtures("refresh_page")
    @allure.title("Test03: Add two product to cart - verify correct information in cart")
    @allure.description(
        "This test adds a product to the cart and verifies the correct information in the cart: name of product,"
        "price display, and total amount")
    def test_verify_product_info_in_cart(self):
        WebFlows.add_product_to_cart(get_data("PRODUCT_ONE"))
        WebFlows.add_two_products_to_cart(get_data("PRODUCT_TWO"))
        WebFlows.click_cart_button()
        WebFlows.verify_cart_information_in_cart(get_data("PRODUCT_ONE"), get_data("PRODUCT_TWO"),
                                                 int(get_data("PRODUCT_ONE_PRICE")),
                                                 int(get_data("PRODUCT_TWO_PRICE")),
                                                 int(get_data("EXPECTED_TOTAL_PRICE_PROD_ONE")),
                                                 int(get_data("EXPECTED_TOTAL_PRICE_PROD_TWO")))

    @pytest.mark.usefixtures("refresh_page")
    @allure.title("Test04: Verify the correct information in the checkout page")
    @allure.description(
        "This test adds a product to the cart and verifies the correct information in the checkout page")
    def test_verify_checkout_page(self):
        WebFlows.add_product_to_cart(get_data("PRODUCT_NAME_CHECK_OUT"))
        WebFlows.proceed_to_checkout_page_flow()
        WebFlows.verify_cart_information_in_table(get_data("PRODUCT_NAME_CHECK_OUT"),
                                                  get_data("EXPECTED_PRICE_PROD_CHECK_OUT"),
                                                  get_data("COUNTER_ONE_PRODUCT"),
                                                  get_data("EXPECTED_TOTAL_PRICE_PROD_CHECK_OUT"))

        WebFlows.verify_cart_information_in_table_middle_page(get_data("EXPECTED_TOTAL_PRICE_PROD_CHECK_OUT"),
                                                              get_data("DISCOUNT"))

    @pytest.mark.usefixtures("main_page")
    @allure.title("Test05: Verify purchase flow with correct promo code")
    @allure.description(
        "This test adds a product to the cart and verifies the promo code is correct & affects the total price")
    def test_verify_promo_code(self):
        WebFlows.add_product_to_cart(get_data("PRODUCT_NAME_CHECK_OUT_CODE"))
        WebFlows.proceed_to_checkout_page_flow()
        WebFlows.apply_promo_code(get_data("CORRECT_PROMO_CODE"))
        WebFlows.verify_purchase_flow_with_correct_promo_code(get_data("SUCCESS_MESSAGE"),
                                                              get_data("EXPECTED_TOTAL_PRICE_PROD_CHECK_OUT_CODE"),
                                                              get_data("DISCOUNT_SUCCESS"),
                                                              get_data("TOTAL_AFTER_DISCOUNT"))

    @pytest.mark.usefixtures("main_page")
    @allure.title("Test06: Negative testing: verify purchase flow with incorrect promo code")
    @allure.description(
        "This test adds a product to the cart and verifies the promo code is not correct & doesn't"
        "affects the total price")
    def test_verify_incorrect_promo_code(self):
        WebFlows.add_product_to_cart(get_data("PRODUCT_NAME_CHECK_OUT_CODE"))
        WebFlows.proceed_to_checkout_page_flow()
        WebFlows.apply_promo_code(get_data("INCORRECT_PROMO_CODE"))
        WebFlows.verify_purchase_flow_with_correct_promo_code(get_data("UNSUCCESS_MESSAGE"),
                                                              get_data("EXPECTED_TOTAL_PRICE_PROD_CHECK_OUT_CODE"),
                                                              get_data("DISCOUNT_UNSUCCESS"),
                                                              get_data("EXPECTED_TOTAL_PRICE_PROD_CHECK_OUT_CODE"))

    @pytest.mark.usefixtures("main_page")
    @allure.title("Test07: Verify purchase flow")
    @allure.description(
        "This test adds a product to the cart and verifies the complete purchase flow")
    def test_verify_purchase_flow(self):
        WebFlows.add_product_to_cart(get_data("PRODUCT"))
        WebFlows.proceed_to_country_page_flow()
        WebFlows.filling_country_page_information_flow(get_data("COUNTRY"))
        WebFlows.verify_successful_order_message(get_data("ORDER_MESSAGE"))

    @pytest.mark.usefixtures("main_page")
    @allure.title("Test08: Verify no results products")
    @allure.description("This test verifies that once there are no results products, the correct message is displayed")
    def test08_verify_no_results_in_search(self):
        WebFlows.verify_no_results_products_display(get_data("SEARCH_INPUT"),
                                                    get_data("NO_RESULTS_LARGE"),
                                                    get_data("NO_RESULTS_SMALL"))
