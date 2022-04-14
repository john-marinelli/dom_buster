from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#TODO filter stdout to reduce visual clutter and useless error messages
#this seems to work, but gets rid of the ability to ctrl+c to quit the session
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])


class InputDriver:
    
    driver = None

    def __init__(self, url, test_input):
        pass
    
    def test_url(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        if input("Press q to quit: \n") == "q":
            return True
        