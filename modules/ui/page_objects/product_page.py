from modules.ui.page_objects.base_page import BasePage


class ProductPage(BasePage):

    xpath_select_product = "//a[contains(@class, 'goods-tile__heading') and contains(@title, 'Apple iPhone 14 Pro Max 128GB')]"
    xpath_enable_price = "//p[contains(@class, 'big product-price')]"
    xpath_find_button_buy = "//button[contains(@class, 'button--green button--medium buy-button--tile')]"

    def select_product(self):
        # Find a product from the list
        goods = self.find_by_xpath(self.xpath_select_product)

        # Click on the product Apple iPhone 14 Pro Max 128GB
        self.driver.get(goods.get_dom_attribute("href"))

    def check_title(self, expected_title):
        # Check the title of the product page
        return expected_title in self.driver.title

    def check_enable_price(self):
        # Check the price is displayed
        is_price_visible = self.find_by_xpath(self.xpath_enable_price).is_displayed()
        return is_price_visible

    def find_button_buy(self):
        # Find the Buy button
        return self.find_by_xpath(self.xpath_find_button_buy)

    def check_enable_button_buy(self):
        # Check that Buy button is displayed
        is_button_visible = self.find_button_buy().is_displayed()
        return is_button_visible

    def click_button_buy(self):
        # Click on the button Buy
        button = self.find_button_buy()
        button.click()