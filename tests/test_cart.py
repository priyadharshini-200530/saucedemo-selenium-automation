from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_shows_added_item(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_driver)
    assert cart_page.get_cart_item_count() == 1
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_remove_item_from_cart_page(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_driver)
    cart_page.remove_backpack()

    assert cart_page.get_cart_item_count() == 0


def test_checkout_button_navigates(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(logged_in_driver)
    cart_page.click_checkout()

    assert "checkout-step-one" in logged_in_driver.current_url