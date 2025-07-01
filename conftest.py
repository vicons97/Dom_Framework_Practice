import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

@pytest.fixture
def driver():
    if os.getenv("GITHUB_ACTIONS") == "true":
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--remote-allow-origins=*")

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def pages(driver):
    class Pages:
        def __init__(self, driver):
            self.home_page = HomePage(driver)
            self.sign_in_page = SignInPage(driver)

    return Pages(driver)

