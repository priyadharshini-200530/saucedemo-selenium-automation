from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    inventory_items = (By.CLASS_NAME, "inventory_item")
    add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    item_prices = (By.CLASS_NAME, "inventory_item_price")

    def add_backpack_to_cart(self):
        self.click(self.add_to_cart_backpack)

    def remove_backpack_from_cart(self):
        self.click(self.remove_backpack)

    def get_cart_count(self):
        return self.get_text(self.cart_badge)

    def sort_products(self, option_value):
        from selenium.webdriver.support.ui import Select
        dropdown = self.driver.find_element(*self.sort_dropdown)
        Select(dropdown).select_by_value(option_value)

    def get_all_prices(self):
        elements = self.driver.find_elements(*self.item_prices)
        return [float(e.text.replace("$", "")) for e in elements]