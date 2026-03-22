from .BasePage import BasePage

class MainPage(BasePage):
    
    TITLE = ".heading" # css selector
    FORK_ME_IMG = "//img[@alt='Fork me on GitHub']" # xpath selector
    LINKS = "//ul/li" # xpath selector
    FORM_AUTHENTICATION = "//a[@href='/login']" # xpath selector
    
    def get_title(self):
        return self.locator(self.TITLE).inner_text()

    def get_fork_me_img(self):
        return self.locator(self.FORK_ME_IMG)

    def get_all_links(self):
        return self.locator(self.LINKS)

    def navigate_to_form_authentication(self):
        self.locator(self.FORM_AUTHENTICATION).click()
    
    def expect_text(self, text: str):
        self.expect_condition(self.locator(self.TITLE), text)
