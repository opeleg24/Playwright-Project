from playwright.sync_api import APIRequestContext
import allure


class APIActions:

    @staticmethod
    @allure.step("GET Request")
    def get(request_context: APIRequestContext):
        api_endpoint = "products.json"
        response = request_context.get(url=api_endpoint)
        return response
