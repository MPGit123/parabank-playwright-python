# from playwright.sync_api import Page
from pages.basepage import BasePage

class LogInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "parabank/index.htm"
        
    def open_parabank_home_page(self):
        self.navigate_to(self.url)