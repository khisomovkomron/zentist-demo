from playwright.sync_api import sync_playwright
from dotenv import load_dotenv  
import os 

load_dotenv() 

class BasePage:
    
    def test_setup(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto(os.getenv("BASE_PAGE"))

if __name__ == "__main__":
    base_page = BasePage()
    base_page.test_setup()