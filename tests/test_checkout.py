
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_complete_checkout_flow(cart_page_checkout):
    
    step_one = CheckoutStepOnePage(cart_page_checkout)
    step_one.fill_checkout_info("Dharshini", "P", "500001")
    step_one.click_continue()

    step_two = CheckoutStepTwoPage(cart_page_checkout)
    assert "Sauce Labs Backpack" in step_two.get_item_names()
    step_two.click_finish()

    complete_page = CheckoutCompletePage(cart_page_checkout)
    assert "Thank you for your order" in complete_page.get_confirmation_message()


def test_checkout_missing_first_name_shows_error(cart_page_checkout):
   
    step_one = CheckoutStepOnePage(cart_page_checkout)
    step_one.fill_checkout_info("", "P", "500001")
    step_one.click_continue()

    assert "First Name is required" in step_one.get_error_text()

def test_checkout_missing_last_name_shows_error(cart_page_checkout):
    
    step_one = CheckoutStepOnePage(cart_page_checkout)
    step_one.fill_checkout_info("Dharshini", "", "500001")
    step_one.click_continue()

    assert "Last Name is required" in step_one.get_error_text()


def test_checkout_missing_zip_code_shows_error(cart_page_checkout):

    step_one = CheckoutStepOnePage(cart_page_checkout)
    step_one.fill_checkout_info("Dharshini", "P", "")
    step_one.click_continue()

    assert "Postal Code is required" in step_one.get_error_text()