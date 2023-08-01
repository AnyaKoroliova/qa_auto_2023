from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class BasePage:
    PATH = r"D://QA Automation (Global Logic)//qa_auto_2023"
    DRIVER_NAME = "chromedriver.exe"
    rzt_tel_number = "093 111 11 11"
    rzt_user_name = "Аня"
    rzt_surname = "Корольова"


    def __init__(self, driver=None):
        if driver is not None:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome(
                service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )

    def find_by_xpath(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except:
            return False
        
    def find_all_by_xpath(self, xpath):
        try:
            return self.driver.find_elements(By.XPATH, xpath)
        except:
            return False

    def close_modal(self):
        close_button = self.driver.find_element(
            By.XPATH, "//button[@class='modal__close']"
        )
        close_button.click()

    def close(self):
        self.driver.close()
