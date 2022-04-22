#John Marinelli, Dillon Shaver
#Univeristy of Colorado: Denver
#Last Updated: 04/21/2022
#Program Purpose:
helpInfo ="""
   This program is an input fuzzer for input boxes on websites. 
   It tests all the inputs on the webpage for crossite scripting vulnerabilities.
   It does so by cycling through a list of payloads and inputting them into all  
   the active and displayed input fields on the webpage and checking for an alert box.  
   
   All default input payloads can be found in the culled_xss_list.txt file inside the res folder.

   Custom payloads can be used by utilizing the custom xss list flag as described below and passing the path to the file.
   *WARNING*: All custom xss files should have each xss input on its own line, otherwise undefined behavior can occur.

   WARNING: Should NOT be tested on websites you do not own or not set up for such purposes for obvious ethical reasons! 
   
   Please use responsibly.

   #--------------------------------------------------------------------------------------------------------------------------------------------
   Syntax and use
   #--------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------
    To get help info:
    #----------------------------------------------------------------------- 
    python3 dom_buster.py -h
        or
    python3 dom_buster.py --help
    #-----------------------------------------------------------------------

    #-----------------------------------------------------------------------
    Run dom_buster on url (no xpath): 
    #-----------------------------------------------------------------------
    python3 dom_buster --u=Your_Url_Path
        or
    python3 dom_buster --url=Your_Url_Path
        or
    python3 dom_buster --URL=Your_Url_Path
    #-----------------------------------------------------------------------

    #-----------------------------------------------------------------------
    Run dom_buster on url with xpath:
    #-----------------------------------------------------------------------
    python3 dom_buster --u=Your_Url_Path --x=Your_Xpath
        or
    python3 dom_buster --url=Your_Url_Path --xpath=Your_Xpath
        or
    python3 dom_buster --URL=Your_Url_Path --XPATH=Your_Xpath
    #-----------------------------------------------------------------------

    #-----------------------------------------------------------------------
    Use Custom xss list (xpath flag also allowed with these calls)
    #-----------------------------------------------------------------------
    python3 dom_buster --u=Your_Url_Path --l=res/path_to_xss_textfile
        or
    python3 dom_buster --url=Your_Url_Path --list=res/path_to_xss_textfile
        or
    python3 dom_buster --URL=Your_Url_Path --LIST=res/path_to_xss_textfile
    #-----------------------------------------------------------------------
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
   Parameters and Options: 
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
   -h : help -description of program use, parameters, and options.
   --url=, --u= : url parameter -Url path to the website to run the payload injection on.
   --xpath=,--x= : [Optional] xpath parameter -Path to the element if input fields is embedded behind buttons or routing. Can be found by copying the xpath from the
                                               webpages source code in the browser's inspect tool.
   --l, --list, --LIST : [Optional] custom xss list parameter: -Path to the text file that holds the custom xss calls you'd like to try on the input boxes
   #-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""

#Notes:
#Google Driver for selenium should be placed in C drive.
#Firefox Driver requires path setup.
from ast import arguments
from sre_constants import SUCCESS
import sys
import getopt
import textwrap
import timeit
from selenium_classes import UrlOpener
from utility import open_payloads, help_open
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def help():
    print(textwrap.dedent(helpInfo))

def main(url_path, xpath_val=None, xpath_flag = False, list_val="res/xss-payload-list.txt", list_flag=False, test=False):
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
                #Types payload to browser input fields, then submits.
                curr_input.send_keys(payload)
                curr_input.submit()
                #Waits for alert message generated by payload, if no alert, no vulnerability detected
                try:
                    WebDriverWait(input_tester.get_driver(), 3).until(EC.alert_is_present(), "")
                    alert = input_tester.get_driver().switch_to.alert
                    alert.accept()
                    id = input_fields[i].get_attribute("innerHTML")
                    alert_count += 1
                    print(f"Alert Found || ID: {id} Payload:{payload} \n")
                    #print("alert detected")
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
    #Pulls arguments from command line
    argList = sys.argv[1:]
    argLen = len(argList)
    #Options for commandline call (string should contain letter for option val, so if options -o, -h, string is "oh:"")
    options = "htuxl:"
    #spelled out options from commandline call (list should contain string of each option. Options with parameters require = sign following option name)
    full_options = ["help","test","url=", "URL=","xpath","list=","LIST="]

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

    # if url != "" and xpath_flag == True:
    #     main(url,xpath,xpath_flag)
    # elif url != "":
    #     main(url)
    if help_flag:
        help()
    elif url_flag and url != "":
        main(url_path=url, xpath_val=xpath, xpath_flag=xpath_flag, list_val=list_path, list_flag=list_flag, test=test_flag)
    else:
        #Account for invalid entry
        print("*INVALID SYNTAX*\n")
        help()

