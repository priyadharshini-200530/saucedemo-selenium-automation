from selenium import webdriver
import pytest
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def driver():
    # Set up the Edge WebDriver
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")  # Open the Sauce Demo website
    yield driver
    driver.quit()