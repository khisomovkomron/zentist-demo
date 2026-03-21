from playwright.sync_api import sync_playwright
from dotenv import load_dotenv  
import os 

load_dotenv() 

class BasePage:
    
    def __init__(self, page):
        self.page = page
