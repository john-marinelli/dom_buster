#John Marinelli, Dillon Shaver
#Univeristy of Colorado: Denver
#Last Updated: 04/21/2022
#Program Purpose:
#This program is meant to weed out DOM XSS vulnerabilities in websites through input fuzzing. 

from ast import arguments
from sre_constants import SUCCESS
import sys
import getopt
import timeit
import logging
from selenium_wrapper import UrlOpener
from utility import import_help_string, open_payloads, help_open, print_help
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def main(url_path, xpath_val=None, xpath_flag = False, list_val="res/xss-payload-list.txt", list_flag=False, test=False, speed_val=3):
    #
    url = url_path
    xpath = xpath_val

    #instantiating the selenium driver class that handles most things
    input_tester = UrlOpener(url)

    alert_count = 0

    #This is the file open function in utility,
    #Retrieves payload information from xss.txt file, 
    #if test flag set (-t), uses shortened list
    payloads = []
    if test:
        payloads = [r"hello", r"123", r"test", r'"><script>alert("hello")</script>', r'anotherone']
    else:
        payloads = open_payloads(list_path)

    #initially load url for input fuzzing
    input_tester.load_url(url)    

    #gets all the input fields on the web page, and how many fields there are
    input_fields = input_tester.list_inputs()
    num_inputs = len(input_fields)

    #Holds all the id's for the input fields
    input_ids = []

    #If there is an xpath, gets the path to the desired input fields
    if xpath_flag is True: 
        if xpath is not None:
            input_tester.pre_xpath(xpath)
    
    #For all dispalyed and active input fields, pull field id's.
    for input in input_fields:
        if input.is_displayed() and input.is_enabled():
            print(input.get_attribute("id"))
            input_ids.append(str(input.get_attribute("id")))

    
    start_time = timeit.default_timer()

    #For all displayed and active input fields, inject and submit payload
    print("Attempting payloads...\n")
    for i in range(num_inputs):
        curr_input = input_fields[i]
        if curr_input.is_displayed() and curr_input.is_enabled():
            for payload in payloads:
                curr_input = input_fields[i]  
                #pressing a button pre-input
                if (xpath_flag):
                    input_tester.pre_xpath(xpath_val)
                #Types payload to browser input fields, then submits. First grabs innerHTML of input box
                #for logging purposes
                id = curr_input.get_attribute("outerHTML")
                curr_input.send_keys(payload)
                curr_input.submit()
                #Waits for alert message generated by payload, if no alert, no vulnerability detected
                try:
                    WebDriverWait(input_tester.get_driver(), speed_val).until(EC.alert_is_present(), "")
                    alert = input_tester.get_driver().switch_to.alert
                    alert.accept()
                    logging.info(f"Alert Found || ID: {id} Payload:{payload} \n")
                    print(f"Alert Found || ID: {id} Payload:{payload} \n")
                    alert_count += 1
                except:
                    pass
                #Navigate back to url (Submit sometimes causes page navigation)
                input_tester.load_url(url)
                #Reget input fields (Some field ID's are unique to individual sessions.)
                input_fields = input_tester.list_inputs()
    
    stop_time = timeit.default_timer()
    execution_time = stop_time-start_time
    if alert_count == 0:
        print(f"All payloads failed.\n")
    
    print(f"Execution time: {execution_time}")

if __name__ == "__main__":

    help_info = import_help_string()
    logging.basicConfig(format='%(asctime)s %(message)s', filename='alerts.log', encoding='utf-8', level=logging.INFO)

    #Pulls arguments from command line
    argList = sys.argv[1:]
    argLen = len(argList)
    #Options for commandline call (string should contain letter for option val, so if options -o, -h, string is "oh:"")
    options = "htuxls:"
    #spelled out options from commandline call (list should contain string of each option. Options with parameters require = sign following option name)
    full_options = ["help","test","url=", "URL=","xpath=", "XPATH=", "list=","LIST=", "speed=", "SPEED="]

    #Concat argument values
    args, vals = getopt.getopt(argList,options,full_options)

    #Variable to store url information
    url = ""
    url_flag = False
    #Variables for xpath entry
    xpath = ""
    xpath_flag = False

    #Variables for custom list input
    list_path = ""
    list_flag = False

    #Variables for help option calls
    help_flag = False

    #Variables for development testing, limits xss calls to 5 for shorter program time
    test_flag = False

    #Parameter for increasing the speed of fuzzing, default is a safe value of 3
    speed_val = 3

    #handle argument logice
    for arg, val in args:
        if arg in ("-h, --help"):
            help_flag = True
        elif arg in ("-u","--url", "--URL"):
            url = val
            url_flag = True
        elif arg in ("-x", "--xpath"):
            xpath = val
            xpath_flag = True
        elif arg in ("-l","--list","--LIST"):
            list_path = val
            list_flag = True
        elif arg in ("-t, --test"):
            test_flag = True
        elif arg in ("-s, --speed, --SPEED"):
            try:
                speed_val=int(val)
            except:
                print("Please enter a valid integer value 1 or above for speed.")

    # if url != "" and xpath_flag == True:
    #     main(url,xpath,xpath_flag)
    # elif url != "":
    #     main(url)
    if help_flag:
        print_help(help_info)
    elif url_flag and url != "":
        main(url_path=url, xpath_val=xpath, xpath_flag=xpath_flag, list_val=list_path, list_flag=list_flag, test=test_flag, speed_val=speed_val)
    else:
        #Account for invalid entry
        print("*INVALID SYNTAX*\n")
        print_help(help_info)

