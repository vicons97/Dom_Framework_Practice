import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()  # this will happen after each test


@pytest.fixture
def pages(driver):

    class Pages:
        def __init__(self, driver):
            self.home_page = HomePage(driver)
            self.sign_in_page = SignInPage(driver)

    return Pages(driver)

