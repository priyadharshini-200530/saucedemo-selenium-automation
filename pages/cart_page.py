from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    cart_items = (By.CLASS_NAME, "cart_item")
    item_names = (By.CLASS_NAME, "inventory_item_name")
    remove_backpack_button = (By.ID, "remove-sauce-labs-backpack")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")

    def get_cart_item_count(self):
        items = self.driver.find_elements(*self.cart_items)
        return len(items)

    def get_item_names(self):
        elements = self.driver.find_elements(*self.item_names)
        return [e.text for e in elements]

    def remove_backpack(self):
        self.click(self.remove_backpack_button)

    def click_checkout(self):
        self.click(self.checkout_button)

    def click_continue_shopping(self):
        self.click(self.continue_shopping_button)