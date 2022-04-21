from twill import commands
from twill import browser
from twill.namespaces import get_twill_glocals
from twill import __url__




class FormGrabber:
    
    _url = ""
    global_dict = {}
    local_dict = {}

    def __init__(self, url):
        self.global_dict, self.local_dict = get_twill_glocals()
        self._url = url
    

    def load_page(self):
        browser.go(self._url)
    
    def show_forms(self):
        browser.showforms()
    
    def input_forms(self, form_num, form_name, input, button):
        commands.formvalue(form_num, form_name, input)
        commands.submit(button)
        """
            Inputs to a specified form on a webpage. 
            Arguments in order: form number, form name, input string, button to press
        """
        self._url = commands.reload()
    
    def show_html(self):
        commands.show()

    def set_url(self, url):
        self._url = url
    
    def get_current_url(self):
        return self._url