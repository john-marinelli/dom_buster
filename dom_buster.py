from selenium_classes import UrlOpener
from utility import open_payloads, help_open
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#TODO switch over input display and selection to selenium
#TODO incorporate URL parameters 
def main():
    url = "https://ac501f3c1fc190c5c08d0ee300490084.web-security-academy.net/"
    xpath = None
    input_tester = UrlOpener(url)
    # payloads = open_payloads()
    payloads = [r"hello", r"123", r"test", r'"><script>alert("hello")</script>', r'anotherone']

    input_tester.load_url(url)    
    input_fields = input_tester.list_inputs()
    num_inputs = len(input_fields)
    input_ids = []

    if xpath is not None:
        input_tester.pre_xpath(xpath)
    
    for input in input_fields:
        if input.is_displayed() and input.is_enabled():
            print(input.get_attribute("id"))
            input_ids.append(str(input.get_attribute("id")))

    for i in range(num_inputs):
        curr_input = input_fields[i]
        if curr_input.is_displayed() and curr_input.is_enabled():
            for payload in payloads:
                curr_input = input_fields[i]
                curr_input.send_keys(payload)
                curr_input.submit()
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

