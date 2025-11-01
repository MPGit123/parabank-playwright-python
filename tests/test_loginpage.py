from pages import LogInPage
import pytest

@pytest.mark.smoke
def test_loginpage(page):
    logInPage = LogInPage(page)
    logInPage.open_parabank_home_page()
    assert page.title() == "ParaBank | Welcome | Online Banking"