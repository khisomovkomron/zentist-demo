from .BasePage import BasePage

class MainPage(BasePage):
    
    TITLE = ".heading"
    FORK_ME_IMG = "//img[@alt='Fork me on GitHub']"
    LINKS = "//ul/li"
    
    def get_title(self):
        return self.locator(self.TITLE).inner_text()

    def get_fork_me_img(self):
        return self.locator(self.FORK_ME_IMG)

    def get_all_links(self):
        return self.locator(self.LINKS)
