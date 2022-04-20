from selenium_classes import UrlOpener
from utility import open_payloads, help_open
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#TODO switch over input display and selection to selenium
#TODO incorporate URL parameters 
def main():
    url = "https://ac7e1fd61fe9fde3c0977f2100c10085.web-security-academy.net/"
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
                #TODO this webdriverwait breaks the program when an alert pops up
                try:
                    WebDriverWait(input_tester.get_driver(), 3).until(EC.alert_is_present(), "Timed out waiting for PA creation " + "confirmation popup to appear")
                    alert = input_tester.get_driver().switch_to.alert
                    alert.accept()
                    print("alert accepted")
                except:
                    print("no alert")
                # if input_tester.alert_check():
                #     print("alert present")
                input_tester.load_url(url)
                input_fields = input_tester.list_inputs()

    #TODO tell if alert is present https://stackoverflow.com/questions/21729464/how-to-check-if-an-alert-is-present-and-if-yes-then-accept-it

    #TODO iterate over inputs
    
    #TODO add check for displayed and interactable 
    #https://stackoverflow.com/questions/30826671/how-to-check-if-an-element-is-clickable-or-not-using-selenium-webdriver


if __name__ == "__main__":
    main()

