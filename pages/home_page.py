from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    #Locators
    login_button = (By.CLASS_NAME, "user-info")
    register_button = (By.XPATH, "//[@class='blockcart cart-preview inactive']")
    username_text = (By.XPATH, "//a[@class='account']/span")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        self.click_element(self.login_button)

    def click_register(self):
        self.click_element(self.register_button)

    def navigate_to_home_page(self):
        self.driver.get("https://teststore.automationtesting.co.uk/index.php")

    def get_username_text(self):
        return self.get_text(self.username_text)