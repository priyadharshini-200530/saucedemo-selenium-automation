from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    zip_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.type_text(self.first_name_field, first_name)
        self.type_text(self.last_name_field, last_name)
        self.type_text(self.zip_code_field, zip_code)

    def click_continue(self):
        self.click(self.continue_button)

    def get_error_text(self):
        return self.get_text(self.error_message)