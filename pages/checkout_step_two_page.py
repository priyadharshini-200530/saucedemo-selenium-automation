from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    finish_button = (By.ID, "finish")
    total_label  = (By.CLASS_NAME, "summary_total_label")
    item_names = (By.CLASS_NAME, "inventory_item_name")

    def click_finish(self):
        self.click(self.finish_button)

    def get_total_text(self):
        return self.get_text(self.total_label)

    def get_item_names(self):
        elements = self.driver.find_elements(*self.item_names)
        return [e.text for e in elements]