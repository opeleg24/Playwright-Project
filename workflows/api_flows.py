from extentions.api_actions import APIActions
import utilities.base as base


class APIFlows:

    @staticmethod
    def get_first_product():
        response = APIActions.get(base.request_context)
        response_json = response.json()
        name = response_json[0]['name']
        return name

    @staticmethod
    def get_amount_of_items():
        response = APIActions.get(base.request_context)
        response_json = response.json()
        return len(response_json)
