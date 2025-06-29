from .base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    #Locators
    email_field = By.NAME,"email"
    password_field = By.NAME,"password"
    submit_btn = By.ID,"submit-login"
    authentication_failed_error = By.CLASS_NAME, "alert-danger"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_sign_in_info(self, email, password):
        self.type_text(self.email_field, email)
        self.type_text(self.password_field, password)
        self.click_element(self.submit_btn)

    def get_authentication_error_text(self):
        return self.get_text(self.authentication_failed_error)
