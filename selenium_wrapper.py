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
    
    #opens url passed at url parameter
    def load_url(self, url):
        self.driver.get(url)

    #Opens Given home url
    def open_home(self):
        self.driver.get(self.home_url)
    
    #Gets all web element objects of inputs on the page, and returns them. (Input boxes like email, pass, name, etc...)
    def list_inputs(self):
        inputs = self.driver.find_elements_by_tag_name("input")
        return inputs

    #Returns driver object 
    def get_driver(self):
        return self.driver
    
    #Gets xpath for browser navigation to get to inputs
    def pre_xpath(self, xpath):
        #this function is meant to allow the program to click on a button 
        #before entering input everytime the page loads
        #This is for more complex webpages (e.g. AirBnB's site)
        #that have a static url, but require a button press before 
        #input
        button = self.driver.find_element_by_xpath(xpath)
        button.click()

