import allure
from smart_assertions import soft_assert


class Verifications:

    @staticmethod
    @allure.step("Verifying equals")
    def verify_equals(actual, expected):
        assert actual == expected, f"Expected: {expected}, but got: {actual}"

    @staticmethod
    @allure.step("Verifying equals using smart assertions")
    def verify_soft_assert_equals(actual, expected, message=None):
        soft_assert(actual == expected, f"Expected: {expected}, but got: {actual} when verifying {message}")

    @staticmethod
    @allure.step("Verifying contains")
    def verify_contains(actual, expected, message=None):
        assert expected in actual, f"Expected: {expected}, but got: {actual} when verifying {message}"
