from modules.ui.page_objects.product_page import ProductPage
from modules.ui.page_objects.category_page import CategoryPage
import pytest
import time


@pytest.mark.ui_rztk
def test_product_page_page_object():

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

    # Check that required product is selected
    assert product_page.check_title("iPhone 14 Pro Max 128GB")
    assert product_page.check_enable_price() == True
    assert product_page.check_enable_button_buy() == True

    # Click on the Buy button
    product_page.click_button_buy()
    time.sleep(3)