from .BasePage import BasePage

class LoginPage(BasePage):
    
    BTN_LOGIN = "button[type='submit']"
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    ERROR_MESSAGE = "//div[@class='flash error']"
    
    def login(self, username: str, password: str):
        self.page.locator(self.USERNAME_FIELD).fill(username)
        self.page.locator(self.PASSWORD_FIELD).fill(password)
        self.page.locator(self.BTN_LOGIN).click()
        
    def error1(self):
        locator = self.page.locator(self.ERROR_MESSAGE)
        locator.wait_for()
        return locator
        

    
