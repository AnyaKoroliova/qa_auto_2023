from modules.ui.page_objects.category_page import CategoryPage
from modules.ui.page_objects.product_page import ProductPage
from modules.ui.page_objects.shopping_cart import CartPage
from modules.ui.page_objects.checkout_page import CheckoutPage
import pytest
import time


@pytest.mark.ui_rztk

def test_checkout_page_object():

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
    time.sleep(3)

    # Click on the Buy button
    product_page.click_button_buy()
    time.sleep(3)

    # Create a shopping cart page object
    shopping_cart = CartPage(driver=category_page.driver)

    # Save the price of the product from the shopping cart
    initial_price = shopping_cart.check_price_is_displayed()

    # Create a checkout page object
    checkout_page = CheckoutPage(driver=category_page.driver)

    # Add a product to the checkout
    checkout_page.add_procuct_to_checkout()
    time.sleep(3)

    # Add the user's phone number
    checkout_page.add_user_tel()
    time.sleep(3)

    # Add the user's lastname
    checkout_page.add_user_surname()

    # Add the user's name
    checkout_page.add_user_name()
    time.sleep(3)

    # Verify that the new user registration button is displayed
    checkout_page.check_register_button_is_displayed() == True

    # Check if the product is displayed
    checkout_page.check_product_displayed() == True

    # Choose a delivery method
    checkout_page.select_delivery()
    time.sleep(3)

    # Choose a payment method
    checkout_page.select_payment()
    time.sleep(3)

    # Check that the price in the checkout is equal to the price of the product
    tot_price, deliv_price = checkout_page.check_checkout_total_delivery_price()
    assert tot_price == initial_price

    # Check the sum of the product price with the shipping cost
    large_price = checkout_page.check_checkout_total_price()
    assert large_price == tot_price + deliv_price