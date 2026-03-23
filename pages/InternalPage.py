from pages.BasePage import BasePage


class InternalPage(BasePage):
    
    TITLE = "h2"
    CONTENT = "#content"
    BTN_LOGOUT = "//a[@href='/logout']"
    
    def get_title_text(self):
        return self.locator(self.TITLE).inner_text()
    
    def get_content(self):
        return self.locator(self.CONTENT)
    
    def get_logout_button(self):
        return self.locator(self.BTN_LOGOUT)
    
    def logout(self):
        self.locator(self.BTN_LOGOUT).click()