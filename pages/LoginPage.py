from .BasePage import BasePage

class LoginPage(BasePage):
    
    BTN_LOGIN = "button[type='submit']"
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    ERROR_MESSAGE = "//div[@class='flash error']" # xpath selector
    SUCCESS_MESSAGE= "div[class='flash success']" # css selector
    
    def login(self, username: str, password: str):
        self.page.locator(self.USERNAME_FIELD).fill(username)
        self.page.locator(self.PASSWORD_FIELD).fill(password)
        self.page.locator(self.BTN_LOGIN).click()
        
    def get_error_message(self):
        locator = self.page.locator(self.ERROR_MESSAGE)
        locator.wait_for()
        return locator
    
    def get_success_message(self):
        locator = self.page.locator(self.SUCCESS_MESSAGE)
        locator.wait_for()
        return locator
    
        

    
