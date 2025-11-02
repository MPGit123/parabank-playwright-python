# from playwright.sync_api import Page
from pages.basepage import BasePage

class LogInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "parabank/index.htm"
        self.usernameBox = page.locator("//input[@name='username']")
        self.passwordBox = page.locator("//input[@name='password']")
        self.loginButton = page.locator("//input[@value='Log In']")
        self.errorMessage = page.locator(".error")
        
    def open_parabank_home_page(self):
        self.navigate_to(self.url)

    def perform_login(self, username, password):
        self.safe_fill(self.usernameBox, username)
        self.safe_fill(self.passwordBox, password)
        self.safe_click(self.loginButton)

    def error_message_text(self):
        return self.errorMessage.inner_text()