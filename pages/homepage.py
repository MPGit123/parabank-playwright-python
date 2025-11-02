from pages.basepage import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_title(self):
        self.page.wait_for_load_state("networkidle")
        return self.page.title()