from input_driver import InputDriver as ID

def main():
    url = "https://ac5a1f621f1519fdc080ac95001f00bd.web-security-academy.net/"
    test_input = "jghgjghg"
    driver = ID(url, test_input)

    driver.input_fuzz_attr()



if __name__ == "__main__":
    main()