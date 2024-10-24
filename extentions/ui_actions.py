import allure
from playwright.sync_api import Locator


class UiActions:

    @staticmethod
    @allure.step("Clicking element")
    def click(locator: Locator):
        locator.click()

    @staticmethod
    @allure.step("Double clicking element")
    def double_click(locator: Locator):
        locator.dblclick()

    @staticmethod
    @allure.step("Clearing text field")
    def clear_text(locator: Locator):
        locator.clear()

    @staticmethod
    @allure.step("Updating text field")
    def update_text(locator: Locator, value):
        locator.fill(value)

    @staticmethod
    @allure.step("Getting text")
    def get_text(locator: Locator):
        return locator.inner_text()

    @staticmethod
    @allure.step("Selecting option from dropdown")
    def select_option(locator: Locator, option):
        locator.select_option(option)

    @staticmethod
    @allure.step("Getting attribute")
    def get_attribute(locator: Locator, attribute):
        return locator.get_attribute(attribute)
