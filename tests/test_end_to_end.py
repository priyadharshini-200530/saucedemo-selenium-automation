from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_full_purchase_journey(logged_in_driver):
    # Step 1: Browse and add multiple items to cart
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == "1"

    # Step 2: Go to cart and verify item is there
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_driver)
    assert cart_page.get_cart_item_count() == 1
    assert "Sauce Labs Backpack" in cart_page.get_item_names()

    # Step 3: Proceed to checkout
    cart_page.click_checkout()

    # Step 4: Fill in checkout information
    step_one = CheckoutStepOnePage(logged_in_driver)
    step_one.fill_checkout_info("Dharshini", "P", "500001")
    step_one.click_continue()

    # Step 5: Verify order summary before finishing
    step_two = CheckoutStepTwoPage(logged_in_driver)
    assert "Sauce Labs Backpack" in step_two.get_item_names()
    step_two.click_finish()

    # Step 6: Verify order confirmation
    complete_page = CheckoutCompletePage(logged_in_driver)
    assert "Thank you for your order" in complete_page.get_confirmation_message()

    # Step 7: Return to products page
    complete_page.click_back_home()
    assert "inventory" in logged_in_driver.current_url