from pages.loginpage import LogInPage
import pytest

'''
This test case is about: TC01: Verify login fails with invalid credentials
'''
@pytest.mark.regression
def test_login_fail_with_invalid_credentials(page, test_data):
    loginPage = LogInPage(page)
    loginPage.open_parabank_home_page()
    loginPage.perform_login(test_data["invalid_username"], test_data["invalid_password"])
    assert loginPage.error_message_text() == "The username and password could not be verified."