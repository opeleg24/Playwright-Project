from playwright.sync_api import APIRequestContext
import pytest
import allure


class APIActions:

    @staticmethod
    @allure.step("GET Request")
    def get(request_context: APIRequestContext):
        api_endpoint = "products.json"
        response = request_context.get(url=api_endpoint)
        return response

    @staticmethod
    @allure.step("Extract value from response")
    def extract_value(response_json, nodes):
        extracted_value = None
        if len(nodes) == 0:
            return response_json
        elif len(nodes) == 1:
            extracted_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extracted_value = response_json[nodes[0]][nodes[1]]
        elif len(nodes) == 3:
            extracted_value = response_json[nodes[0]][nodes[1]][nodes[2]]
        return extracted_value
