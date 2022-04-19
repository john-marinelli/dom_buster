import webbrowser


def help_open():
    webbrowser.open("www.github.com") #TODO add github page

def open_payloads(path="res/xss-payload-list.txt"):
    payloads = []
    with open(path) as file:
        payloads = file.readlines()
    for i in range(len(payloads)):
        payloads[i] = payloads[i].strip()
    return payloads


        