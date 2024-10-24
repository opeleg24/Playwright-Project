import pytest
import allure

from extentions.api_actions import APIActions
from extentions.verifications import Verifications
from utilities.common_ops import get_data
from workflows.api_flows import APIFlows


@pytest.mark.usefixtures('init_api')
class Test_API:

    @allure.title("Test01: Verify initial amount of items & products in header display")
    @allure.description("This test verifies the initial amount of items & products in the header display")
    def test_verify_initial_header_amount(self):
        name_of_product = APIFlows.get_first_product()
        Verifications.verify_equals(name_of_product, get_data("PRODUCT_NAMR_API"))
