import json
import time

import pytest
from playwright.sync_api import Playwright

from utilities.base import Base

from utilities import base
from utilities.common_ops import get_data


@pytest.fixture(scope='class')
def init_page(playwright: Playwright):
    browser_type = get_data('BROWSER_TYPE').lower()
    slow_motion = int(get_data('SLOW_MODE'))
    if browser_type == "chrome":
        base.browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=slow_motion)
    elif browser_type == "firefox":
        base.browser = playwright.firefox.launch(headless=False, channel="firefox", slow_mo=slow_motion)
    elif browser_type == "edge":
        base.browser = playwright.webkit.launch(headless=False, channel="msedge", slow_mo=slow_motion)
    base.context = base.browser.new_context()
    # Start tracing before creating a context
    base.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    base.page = base.context.new_page()
    base.page.set_default_timeout(150000)
    Base.init_pages()
    base.page.goto(get_data('BASE_URL'))

    yield
    # time.sleep(3)
    base.context.tracing.stop(path="trace.zip")
    base.context.close()
    base.browser.close()


@pytest.fixture(scope='class')
def init_api(playwright: Playwright):
    base.request_context = playwright.request.new_context(
        base_url=get_data("BASE_URL_API"))

    yield
    base.request_context.dispose()


@pytest.fixture()
def refresh_page():
    base.page.reload()


@pytest.fixture()
def main_page():
    base.page.goto(get_data('BASE_URL'))

# def pytest_exception_interact(node, call, report):
#     if report.failed:
#         # if globals()['driver'] is not None:  # if it is None-> this is for API tests
#         # image = "./playwright_project/screen-shots/screen_" + str(get_time_stamp()) + ".png"
#         image_path = "./screen-shots/screen.png"
#         image = base.page.screenshot(path=image_path, full_page=True)
#         allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)
