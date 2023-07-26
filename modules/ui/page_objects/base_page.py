from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    PATH = r'D://QA Automation (Global Logic)//qa_auto_2023'
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(BasePage.PATH + BasePage.DRIVER_NAME))

    def close(self):
        self.driver.close()