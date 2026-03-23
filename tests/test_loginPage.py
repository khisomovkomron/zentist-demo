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
        
        expect(loginPage.get_error_message()).to_contain_text("Your password is invalid!")

    @pytest.mark.parametrize("username, password, error_message", [
        ("tomsmith", "wrong", "Your password is invalid!"), 
        ("invalid", "SuperSecretPassword!", "Your username is invalid!"), 
        (" ", " ", "Your username is invalid!")])
    def test_login_negative_cases(self, mainPage, loginPage, username, password, error_message):
        mainPage.goto(os.getenv("MAIN_PAGE"))
        mainPage.navigate_to_form_authentication()
        loginPage.login(username, password)
        
        expect(loginPage.get_error_message()).to_contain_text(error_message)
        
    '''
    Scenario 3 - Login to the site
        Open Login page
        Login with valid credentials
        Assert user in on the /security page
        Assert page has title and content
        Assert page has “Logout” button
        Logout
        Assert user logged out
    '''
    def test_login_positive_case(self, mainPage, loginPage, internalPage):
        loginPage.goto(os.getenv("LOGIN_PAGE"))
        loginPage.login(username="tomsmith", password="SuperSecretPassword!")
        expect(loginPage.get_success_message()).to_contain_text(" You logged into a secure area!")
        
        assert "secure" in internalPage.page.url

        assert internalPage.get_title_text() == "Secure Area"
        expect(internalPage.get_content()).to_be_visible()
        
        expect(internalPage.get_logout_button()).to_be_visible()
        
        internalPage.logout()
        expect(loginPage.get_success_message()).to_contain_text("You logged out of the secure area!")

        