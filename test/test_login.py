import allure
import pytest



@allure.title("Make test of login successful")
@allure.severity("Critical")
@allure.feature("Sign In")
@pytest.mark.regression
def test_login_success(pages):


    with allure.step("Navigate to main page"):
        pages.home_page.navigate_to_home_page()
    
    with allure.step("Make click in login"):
        pages.home_page.click_login()

    with allure.step("input sign in info"):
        pages.sign_in_page.enter_sign_in_info("test@test.com", "test123")

    with allure.step("get user name once logged in"):
        username_text = pages.home_page.get_username_text()
        assert username_text == "John Smith"
