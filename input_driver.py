from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#TODO filter stdout to reduce visual clutter and useless error messages
#this seems to work, but gets rid of the ability to ctrl+c to quit the session
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])


class InputDriver:
    
    driver = None
    home_url = None
    current_url = None
    html_source = None
    test_input = None
    #attributes = []
    input_fields = ""

    def __init__(self, url, test_input):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.home_url = self.driver.current_url
        self.current_url = self.home_url
        self.input_fields = self.driver.find_elements_by_tag_name('input')
        self.test_input = test_input
    
    def input_fuzz_attr(self):

        for box in self.input_fields:
            box.send_keys(self.test_input)
            box.submit()
            WebDriverWait(self.driver, 15).until(EC.url_changes(self.current_url))
            self.current_url = self.driver.current_url
            #TODO check for dom changes, url stuff for XSS

            html_source = self.driver.page_source
            soup = BeautifulSoup(html_source, 'html.parser')
            i = 0
            for node in soup.find_all():
                if any(self.test_input in i for i in node.attrs.values()):
                    print("Input found in an html element's attributes")
                    i += 1
            #print("Input was found in " + i "html element's attributes.")
            self.driver.get(self.home_url)
            self.current_url = self.home_url
    
    def input_fuzz_text(self):
        #TODO figure out how to check for input escaping
        for box in self.input_fields:
            box.send_keys(self.test_input)
            box.submit()
            WebDriverWait(self.driver, 15).until(EC.url_changes(self.current_url))
            self.current_url = self.driver.current_url
            #TODO check for dom changes, url stuff for XSS

            html_source = self.driver.page_source
            soup = BeautifulSoup(html_source, 'html.parser')
            i = 0
            for node in soup.find_all():
                if self.test_input in node.text:
                    print("Input found in an html element's text.")
                    i += 1
            #print("Input was found in " + i "html element's attributes.")
            self.driver.get(self.home_url)
            self.current_url = self.home_url