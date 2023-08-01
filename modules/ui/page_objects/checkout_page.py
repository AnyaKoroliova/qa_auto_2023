from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.shopping_cart import CartPage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    xpath_add_tel = "//input[contains(@data-testid, 'cart-counter-input')]"
    xpath_add_user_name = "//rz-checkout-contact-info//input[@formcontrolname='name']"
    xpath_add_surname = "//rz-checkout-contact-info//input[@formcontrolname='surname']"
    xpath_ref_button = "//button[contains(@class, 'checkout-total__submit')]"
    xpath_small_product = "//a[contains(@class, 'checkout-product__title')]"
    xpath_total_price_large = "//dd[contains(@class, 'checkout-total__value_size_large')]"
    xpath_select_delivery = "//rz-checkout-order-deliveries//rz-checkout-order-delivery"
    xpath_select_pay = "//rz-checkout-order-payments//rz-checkout-order-payment"
    xpath_check_tot_price = "//dd[@class='checkout-total__value']"



    def add_procuct_to_checkout(self):
        # Add a product from the shopping cart to the checkout
        order_btn = self.find_by_xpath(CartPage.xpath_check_submit_order_button)
        order_btn.click()

    def add_user_tel(self):
        # Add the user's phone number
        user_tel =self.driver.find_element(By.ID, 'checkoutUserPhone').send_keys(self.rzt_tel_number)
        return user_tel
    
    def add_user_surname(self):
        # Add the user's lastname
        user_surname = self.find_by_xpath(self.xpath_add_surname).send_keys(self.rzt_surname)
        return user_surname
    
    def add_user_name(self):
        # Add the user's name
        user_name = self.find_by_xpath(self.xpath_add_user_name).send_keys(self.rzt_user_name)
        return user_name
    
    def check_register_button_is_displayed(self):
        # Verify that the new user registration button is displayed
        try:
            reg_btn = self.find_by_xpath(self.xpath_ref_button)
            return reg_btn.is_displayed()
        except:
            return False
        
    def check_product_displayed(self):
        # Check if the product is displayed
        try:
            small_product = self.find_by_xpath(self.xpath_small_product)
            return small_product.is_displayed()
        except:
            return False
        
    def select_delivery(self):
        # Choose a delivery method
        delivs = self.find_all_by_xpath(self.xpath_select_delivery)
        if len(delivs) >= 2:
            deliv = delivs[1]
            deliv.click()

    def select_payment(self):
        # Choose a payment method
        pays = self.find_all_by_xpath(self.xpath_select_pay)
        if len(pays) >= 5:
            pay = pays[4]
            pay.click()

    def check_checkout_total_delivery_price(self):
        # Return the price of the product and the cost of shipping
        total_prices = self.find_all_by_xpath(self.xpath_check_tot_price)
        if len(total_prices) >1:
            total_price = str(total_prices[0].text).replace('₴', '').replace(' ', '')
            delivery_price = str(total_prices[1].text).replace('₴', '').replace(' ', '')

        return float(total_price),float(delivery_price)
    
    def check_checkout_total_price(self):
        # Find the total price
        total = self.find_by_xpath(self.xpath_total_price_large)
        t = str(total.text).replace('₴', '').replace(' ', '')
        return float(t)