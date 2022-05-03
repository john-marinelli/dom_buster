import webbrowser
import re
import textwrap

#Utility file for various helper functions

#Hoping to open a readme webpage with the --help option
def help_open():
    webbrowser.open("www.github.com") #TODO add github page

#open payloads file
def open_payloads(path="res/xss-payload-list.txt"):
    payloads = []
    with open(path) as file:
        payloads = file.readlines()
    for i in range(len(payloads)):
        payloads[i] = payloads[i].strip()
    return payloads

def import_help_string():
    with open("res/help_info.txt", encoding='utf-8') as file:
        help_info = file.read()
    return help_info

def print_help(help_info):
    print(textwrap.dedent(help_info))