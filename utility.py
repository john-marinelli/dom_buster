import webbrowser
import re

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


#function to cull data to find only payloads with "alert" in them
# def data_culling():
#     lines = []
#     to_find = re.compile("alert")
#     j = 0
#     #TODO RE of 'alert' instead of is "" in
#     with open("res/xss-payload-list.txt") as file:
#         lines = file.readlines()

#     while j < len(lines):

#         if :
#             lines.pop(j)
        
#         j += 1
    
#     with open("res/culled_xss_list.txt", "w") as file:
#         file.writelines(lines)


if __name__ == "__main__":
    data_culling()