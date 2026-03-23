from dotenv import load_dotenv  
import os 
from playwright.sync_api import expect  
import logging

logger = logging.getLogger(__name__)
load_dotenv() 

class BasePage:
    
    def __init__(self, page):
        self.page = page
        
    def goto(self, endpoint=""):
        url = os.getenv("BASE_URL") + endpoint
        logger.info(f"Navigating to {url}")
        self.page.goto(url)
        
    def get_title(self):
        return self.page.title()
    
    def locator(self, selector):
        return self.page.locator(selector)
    
    def expect_condition(self, locator, text: str):
        return expect(locator).to_have_text(text)
