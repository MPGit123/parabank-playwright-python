from pages.loginpage import LogInPage
import pytest

'''
This test case is about: TC01: Verify login fails with invalid credentials
'''
@pytest.mark.smoke
def test_login_success_with_valid_credentials(page, test_data):
    loginPage = LogInPage(page)
    loginPage.open_parabank_home_page()
    homePage = loginPage.perform_login(test_data["valid_username"], test_data["valid_password"])
    assert homePage.page_title() == "ParaBank | Accounts Overview"