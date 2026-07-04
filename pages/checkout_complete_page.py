from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    complete_header = (By.CLASS_NAME, "complete-header")
    back_home_button = (By.ID, "back-to-products")

    def get_confirmation_message(self):
        return self.get_text(self.complete_header)

    def click_back_home(self):
        self.click(self.back_home_button)