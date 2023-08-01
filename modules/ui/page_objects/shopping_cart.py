from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    xpath_find_modal_win = "//rz-single-modal-window"
    xpath_select_mini_cart = "//button[contains(@class, 'header__button--active')]"
    xpath_product_is_displayed = "//div[@class = 'cart-product__body']"
    xpath_find_price = "//p[contains(@class, 'cart-product__price')]"
    xpath_update_product_qnt = "//input[contains(@data-testid, 'cart-counter-input')]"
    xpath_delete_product = "//button[@class = 'button button--medium button--with-icon button--link']"
    xpath_check_submit_order_button = "//a[@data-testid = 'cart-receipt-submit-order']"

    def find_modal_window(self):
        # Find the Shopping cart window
        return self.find_by_xpath(self.xpath_find_modal_win)

    def check_is_displayed_cart_window(self):
        # Check that the shopping cart window is displayed
        try:
            is_window_visible = self.find_modal_window()
            return is_window_visible.is_displayed()
        except:
            return False

    def check_header_button(self):
        # Click on the mini-cart in the header
        header_button = self.find_by_xpath(self.xpath_select_mini_cart)
        header_button.click()

    def check_product_is_displayed(self):
        # Check if the product is displayed
        try:
            prd_blc = self.find_by_xpath(self.xpath_product_is_displayed)
            return prd_blc.is_displayed()
        except:
            return False
    
    def check_price_is_displayed(self):
        # Check that the price is displayed
        price = self.find_by_xpath(self.xpath_find_price)
        p = str(price.text).replace('₴', '').replace(' ', '')
        return float(p)

    def delete_product_qnt(self):
        # Remove the amount of the product in the shopping cart
        delete_qnt = self.find_by_xpath(self.xpath_update_product_qnt).clear()
        return delete_qnt
    
    def update_product_qnt(self):
        # Update the quantity of the product in the shopping cart
        prd_qnt = self.find_by_xpath(self.xpath_update_product_qnt).send_keys('2')
        return prd_qnt
    
    def check_submit_order_button(self):
        # Check if the Checkout button is displayed
        try:
            order = self.find_by_xpath(self.xpath_check_submit_order_button)
            return order.is_displayed()
        except:
            return False
    
    def delete_product_from_cart(self):
        # Remove product from shopping cart
        button_del = self.driver.find_element(By.ID, 'cartProductActions0')
        button_del.click()
        del_prd = self.find_by_xpath(self.xpath_delete_product)
        del_prd.click()