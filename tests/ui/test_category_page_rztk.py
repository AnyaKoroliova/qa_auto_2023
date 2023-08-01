from modules.ui.page_objects.category_page import CategoryPage
import pytest
import time


@pytest.mark.ui_rztk
def test_open_category_page_page_object():

    # Create a category page object
    category_page = CategoryPage()

    # Open page https://rozetka.com.ua/
    category_page.go_to()

    # Go to category
    category_page.choose_category()

    time.sleep(3)
    # Check that the filter works correctly
    assert category_page.check_title("Apple iPhone")
    assert category_page.check_active_checkbox().strip() == "Apple"
    assert category_page.check_products_availability() == 29

    time.sleep(3)

    # Select the filter by phone series
    category_page.select_filters()

    time.sleep(3)
    # Check that only iPhone 14 Pro Max series products are displayed on the page
    assert category_page.check_title("iPhone 14 Pro Max")
