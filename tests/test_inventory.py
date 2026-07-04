
from pages.inventory_page import InventoryPage
from selenium.common.exceptions import TimeoutException


def test_add_item_to_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_remove_item_from_cart(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    try:
        inventory_page.get_cart_count()
        assert False, "Cart badge should not exist after removing item"
    except TimeoutException:
        assert True


def test_sort_price_low_to_high(logged_in_driver):
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.sort_products("lohi")
    prices = inventory_page.get_all_prices()

    assert prices == sorted(prices)