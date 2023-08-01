from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class CategoryPage(BasePage):
    URL = "https://rozetka.com.ua/"

    xpath_choose_required_category = "//a[contains(@href, 'telefony-tv-i-ehlektronika') and contains(@class, 'menu-categories')]"
    xpath_choose_apple_category = "//a[contains(@href, 'mobile-phones/c80003/producer=apple') and contains(@class, 'popular-category')]"
    xpath_select_apple_checkbox = "//a[contains(@class, 'checkbox-filter__link') and contains(@data-id, 'iPhone 14 Pro Max')]"
    xpath_check_apple_checkbox_active = "//a[contains(@class, 'checked') and contains(@data-id, 'Apple')]"
    xpath_products_available = "//a[contains(@class, 'goods-tile__heading') and contains(@title, 'Apple')]"
 
    def go_to(self):
        self.driver.get(CategoryPage.URL)

    def choose_category(self):
        # Find the Catalog button
        btn_catalog = self.driver.find_element(By.ID, "fat-menu")

        # Click on the Catalog button
        btn_catalog.click()

        # Находим категорию Смартфоны, ТВ и электроника
        btn_category = self.find_by_xpath(self.xpath_choose_required_category)

        # Find the category Smartphones, TV and electronics
        btn_category.click()
        time.sleep(3)

        # Find the Apple category
        btn_apple = self.find_by_xpath(self.xpath_choose_apple_category)

        # Click on the category Apple
        btn_apple.click()

    def check_title(self, expected_title):
        # Check the Category Title
        return expected_title in self.driver.title

    def check_products_availability(self):
        # Check that only Apple products are displayed on the product page
        prd = self.find_all_by_xpath(self.xpath_products_available)
        return len(prd)

    def select_filters(self):
        # Find a filter by phone series
        btn_filter = self.find_by_xpath(self.xpath_select_apple_checkbox)
        # Нажимаем на фильтр iPhone 14 Pro Max
        btn_filter.click()

    def check_active_checkbox(self):
        # Verify that the required checkbox is selected
        btn_checkbox = self.find_by_xpath(self.xpath_check_apple_checkbox_active)
        return btn_checkbox.get_dom_attribute("data-id")
