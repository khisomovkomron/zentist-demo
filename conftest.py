from playwright.sync_api import sync_playwright
import pytest
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from pages.InternalPage import InternalPage
import logging
import allure

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    logger.info("Browser launched")
    page = browser.new_page()
    logger.info("New page created")
    yield page
    page.close()
    logger.info("Page closed")
    browser.close()
    logger.info("Browser closed")
    playwright.stop()


@pytest.fixture
def basePage(browser):
    return BasePage(browser)

@pytest.fixture
def mainPage(browser):
    return MainPage(browser)

@pytest.fixture
def loginPage(browser):
    return LoginPage(browser)

@pytest.fixture
def internalPage(browser):
    return InternalPage(browser)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs['browser']
        screenshot = page.screenshot()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)