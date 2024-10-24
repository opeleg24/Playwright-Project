from playwright.sync_api import Page


class CountryPage:
    def __init__(self, page: Page):
        self.page = page
        self.select_country = self.page.locator("select")
        self.terms_conditions_checkbox = self.page.locator("[class='chkAgree']")
        self.proceed_button = self.page.locator("text=Proceed")
        self.success_message = self.page.locator("[class='products'] span").first

    def get_select_country(self):
        return self.select_country

    def get_terms_conditions_checkbox(self):
        return self.terms_conditions_checkbox

    def get_proceed_button(self):
        return self.proceed_button

    def get_success_message(self):
        return self.success_message
