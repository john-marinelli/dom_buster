from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#This class needs to be refactored to accurately reflect what it does
#I'm planning on doing some organizational work on it, but it does
#work as intended currently


class UrlOpener:
    
    driver = None
    home_url = None

    def __init__(self, home_url):
        self.driver = webdriver.Chrome()
        self.home_url = home_url
    
    def load_url(self, url):
        self.driver.get(url)
    
    def open_home(self):
        self.driver.get(self.home_url)

    def visit_url(self, url):
        self.driver.get()
    
    def list_inputs(self):
        inputs = self.driver.find_elements_by_tag_name("input")
        return inputs

    def get_driver(self):
        return self.driver
    
    def pre_xpath(self, xpath):
        
        button = self.driver.find_elements_by_xpath(xpath)
        button.click()

    def alert_check(self):
        try:
            self.driver.switch_to().alert().accept()
            return True
        except:
            return False

