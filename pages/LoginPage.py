from .BasePage import BasePage

class LoginPage(BasePage):
    
    BTN_LOGIN = "button[type='submit']" # css selector
    USERNAME_FIELD = "#username" # css selector
    PASSWORD_FIELD = "#password" # css selector
    ERROR_MESSAGE = "//div[@class='flash error']" # xpath selector
    SUCCESS_MESSAGE= "div[class='flash success']" # css selector
    
    def login(self, username: str, password: str):
        self.locator(self.USERNAME_FIELD).fill(username)
        self.locator(self.PASSWORD_FIELD).fill(password)
        self.locator(self.BTN_LOGIN).click()
        
    def get_error_message(self):
        locator = self.locator(self.ERROR_MESSAGE)
        locator.wait_for()
        return locator
    
    def get_success_message(self):
        locator = self.locator(self.SUCCESS_MESSAGE)
        locator.wait_for()
        return locator
    
        

    
