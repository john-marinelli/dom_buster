from selenium_classes import UrlOpener
from utility import open_payloads, help_open
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#TODO switch over input display and selection to selenium
#TODO incorporate URL parameters 
def main():
    url = "https://facebook.com"
    xpath = None
    input_tester = UrlOpener(url)
    # payloads = open_payloads()
    payloads = ["hello", "123", "test"]

    input_tester.load_url(url)    
    input_fields = input_tester.list_inputs()
    input_ids = []

    if xpath is not None:
        input_tester.pre_xpath(xpath)
    
    for input in input_fields:
        if input.is_displayed() and input.is_enabled():
            print(input.get_attribute("id"))
            input_ids.append(str(input.get_attribute("id")))

    for input in input_ids:
        for payload in payloads:
            element = input_tester.get_driver().find_element(By.ID, input)
            element.send_keys(payload)
            element.submit()
            WebDriverWait(input_tester.get_driver(), 10).until(EC.url_changes(url))
            if input_tester.alert_check():
                print("alert present")
            input_tester.load_url(url)

    #TODO tell if alert is present https://stackoverflow.com/questions/21729464/how-to-check-if-an-alert-is-present-and-if-yes-then-accept-it

    #TODO iterate over inputs
    
    #TODO add check for displayed and interactable 
    #https://stackoverflow.com/questions/30826671/how-to-check-if-an-element-is-clickable-or-not-using-selenium-webdriver


if __name__ == "__main__":
    main()