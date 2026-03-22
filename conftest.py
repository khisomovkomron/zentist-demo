from playwright.sync_api import sync_playwright
import pytest
from pages.BasePage import BasePage
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    page.close()
    browser.close()
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
