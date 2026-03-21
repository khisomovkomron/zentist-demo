from dotenv import load_dotenv  
import os 

load_dotenv() 

class BasePage:
    
    def __init__(self, page):
        self.page = page
        
    def goto(self, endpoint=""):
        url = os.getenv("BASE_URL") + endpoint
        self.page.goto(url)
        
    def get_title(self):
        return self.page.title()
    
    def locator(self, selector):
        return self.page.locator(selector)
