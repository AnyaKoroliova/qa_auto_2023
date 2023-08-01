from modules.ui.page_objects.category_page import CategoryPage
from modules.ui.page_objects.product_page import ProductPage
from modules.ui.page_objects.shopping_cart import CartPage
import pytest
import time


@pytest.mark.ui_rztk
def test_shopping_page_page_object():

    # Create a category page object
    category_page = CategoryPage()

    # Open page https://rozetka.com.ua/
    category_page.go_to()

    # Go to category
    category_page.choose_category()
    time.sleep(3)

    # Select the filter by phone series
    category_page.select_filters()
    time.sleep(3)

    # Create a product page object
    product_page = ProductPage(driver=category_page.driver)

    # Go to the product from the category page
    product_page.select_product()

    # Click on the Buy button
    product_page.click_button_buy()
    time.sleep(1)

    # Create a shopping cart page object
    shopping_cart = CartPage(driver=category_page.driver)

    # Check that the shopping cart window is displayed
    assert shopping_cart.check_is_displayed_cart_window() == True

    # Close shopping cart window
    shopping_cart.close_modal()
    time.sleep(1)

    # Check that the shopping cart window is not displayed
    assert shopping_cart.check_is_displayed_cart_window() == False

    # Click on the mini-cart in the header
    shopping_cart.check_header_button()
    time.sleep(3)

    # Check that the shopping cart window is displayed and the product is displayed in the window
    assert shopping_cart.check_is_displayed_cart_window() == True
    assert shopping_cart.check_product_is_displayed() == True

    # Check that the price is displayed
    old_price = shopping_cart.check_price_is_displayed()

    # Remove the amount of the product in the shopping cart
    shopping_cart.delete_product_qnt()

    # Update the quantity of the product in the shopping cart
    shopping_cart.update_product_qnt()
    time.sleep(3)

    # Check that the price has doubled after updating the quantity of the product in the shopping cart
    new_price = shopping_cart.check_price_is_displayed()
    assert new_price == old_price * 2

    # Check if the Checkout button is displayed
    shopping_cart.check_submit_order_button() == True

    # Remove product from shopping cart
    shopping_cart.delete_product_from_cart()
    time.sleep(3)

    # Check that the cart is empty
    assert shopping_cart.check_product_is_displayed() == False

    # Close shopping cart window
    shopping_cart.close_modal()
    time.sleep(1)
    
    # Click on the Buy button
    product_page.click_button_buy()
    time.sleep(3)

    # Check that the shopping cart window is displayed
    assert shopping_cart.check_is_displayed_cart_window() == True