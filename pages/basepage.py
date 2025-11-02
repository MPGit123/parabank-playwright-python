from playwright.sync_api import Page
from config.settings import settings

class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.page.set_default_timeout(settings.default_timeout_ms)

    def navigate_to(self, url_text: str):
        self.page.goto(settings.base_url + url_text)
        self.page.wait_for_load_state("networkidle")

    def safe_fill(self, locator, text):
        locator.wait_for(state="visible")
        locator.fill(text)

    def safe_click(self, locator):
        locator.wait_for(state="visible")
        locator.click()