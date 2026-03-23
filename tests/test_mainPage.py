import pytest
from dotenv import load_dotenv  
import os 
import logging

logger = logging.getLogger(__name__)
load_dotenv() 

class TestMainPage:
    '''
    Scenario 1 - Main Page
        Open Main Page
        Assert page has title
        Assert page has ‘Fork me on Github’ element
        Assert page content contains 44 links
    '''

    # реализовал 2 сценарие в разных тестах, можно скомбинироват в один, но так будет лучше для ассертов
    
    def test_site_is_accessible(self, mainPage):
        mainPage.goto(os.getenv("MAIN_PAGE"))
        assert mainPage.get_title() != ""
        mainPage.expect_text("Welcome to the-internet")
        
    def test_page_has_for_me_element(self, mainPage):
        mainPage.goto("/")
        assert mainPage.get_fork_me_img().is_visible()
        
    def test_page_has_links(self, mainPage):
        mainPage.goto("/")
        links = mainPage.get_all_links()
        assert links.count() > 0
        assert links.count() == 44
        