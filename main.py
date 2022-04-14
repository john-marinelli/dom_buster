from input_driver import InputDriver as ID
from twill_ui import FormGrabber

def main():
    url = "https://acdf1fab1f30670ac0ee982300ee006f.web-security-academy.net/"
    form_name = ""
    test_input = "\"><script>alert(1)</script>"
    form_grabber = FormGrabber(url)
    input_tester = ID(url, test_input)
    


    form_grabber.load_page()
    form_grabber.show_forms()
    print(form_grabber.get_current_url())
    form_num = input("Select form number: \n")
    form_name = input("Select form name (leave blank if none): \n")
    button = input("Select button to press: \n")
    form_grabber.input_forms(form_num, form_name, test_input, button)
    print(form_grabber.get_current_url())

    input_tester.test_url(str(form_grabber.get_current_url()))



if __name__ == "__main__":
    main()