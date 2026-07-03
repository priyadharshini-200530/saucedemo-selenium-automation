
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_password")
    error = login_page.get_error_text()
    assert "Username and password do not match" in error