from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click(self.login_button)

    def get_error_text(self):
        return self.get_text(self.error_message)