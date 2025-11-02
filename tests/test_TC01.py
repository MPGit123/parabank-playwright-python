from pages import LogInPage
import pytest

'''
This test case is about: TC01: Verify homepage loads successfully
'''
@pytest.mark.smoke
def test_loginpage_loads_successfully(page):
    logInPage = LogInPage(page)
    logInPage.open_parabank_home_page()
    assert page.title() == "ParaBank | Welcome | Online Banking"