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

    # реализовал сценарие 2 в разных тестах, можно скомбинироват в один, но так будет лучше для ассертов
    
    def test_site_is_accessible(self, mainPage):
        logger.info("________ Testing if the site is accessible")
        mainPage.goto(os.getenv("MAIN_PAGE"))
        assert mainPage.get_title() != ""
        assert mainPage.get_heading_text() == "Welcome to the-internet"
        
    def test_page_has_for_me_element(self, mainPage):
        logger.info("________ Testing if the page has 'Fork me on Github' element")
        mainPage.goto(os.getenv("MAIN_PAGE"))
        assert mainPage.get_fork_me_img().is_visible()
        
    def test_page_has_links(self, mainPage):
        logger.info("________ Testing if the page has 44 links")
        mainPage.goto(os.getenv("MAIN_PAGE"))
        links = mainPage.get_all_links()
        assert links.count() > 0
        assert links.count() == 44
        