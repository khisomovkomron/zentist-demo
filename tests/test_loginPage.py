import pytest
from dotenv import load_dotenv  
import os 
from playwright.sync_api import expect  

load_dotenv() 

class TestLoginPage:
    '''
    Scenario 2 - Login Page
        Open Main Page
        Navigate to Login Page by clicking on ‘Form Authentication’ link
        Automate sufficient amount of test cases to make sure it’s impossible to login by providing invalid credentials

    '''
    
    def test_login_negative_case(self, mainPage, loginPage):
        mainPage.goto(os.getenv("MAIN_PAGE"))
        mainPage.navigate_to_form_authentication()
        loginPage.login(username="tomsmith", password="wrong")
        
        expect(loginPage.error1()).to_contain_text("Your password is invalid!")

    @pytest.mark.parametrize("username, password, error_message", [
        ("tomsmith", "wrong", "Your password is invalid!"), 
        ("invalid", "SuperSecretPassword!", "Your username is invalid!"), 
        (" ", " ", "Your username is invalid!")])
    def test_login_negative_cases(self, mainPage, loginPage, username, password, error_message):
        mainPage.goto(os.getenv("MAIN_PAGE"))
        mainPage.navigate_to_form_authentication()
        loginPage.login(username, password)
        
        expect(loginPage.error1()).to_contain_text(error_message)