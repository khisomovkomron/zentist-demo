import pytest
from dotenv import load_dotenv  
import os 

load_dotenv() 

class TestMainPage:
    
    def test_site_is_accessible(self, browser):
        browser.goto(os.getenv("BASE_PAGE"))
        assert browser.title() != ""
        
        