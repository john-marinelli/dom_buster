# Dom Buster

## Overview:

Dom Buster is a tool used for testing websites for cross-site scripting vulnerabilities, with a particular emphasis on those having to do with the Document Object Model.

It's a dynamic analysis tool that treats a website as a black box, simulating repeated cross-site scripting attempts and reporting back vulnerabilities.

Dom Buster does not require any access to your code base.

## Installation:

Dom Buster uses Selenium and chromedriver to search and interact with webpages. In order to start using the program, you must install both of these.

### Install Selenium:

```

pip3 install selenium

```

### Install chromedriver using a package manager (recommended): 


On Windows you can use Chocolatey:

```

choco install chromedriver

```


On Mac OS, we recommend using Homebrew:

```

brew --cask install chromedriver

```

On Debian based Linux distributions, you can find chromedriver on apt:

```

sudo apt install chromium-chromedriver

```

### Manually install chromedriver:

One issue with using a package manager is that some versions of chromedriver they distribute may lag behind chrome updates.
You must make sure that your chrome version matches the chromedriver version you download. If a chromedriver download from one of these package managers is of the incorrect version, you can always find the latest at https://chromedriver.chromium.org/.

After downloading:

On Linux make sure you make the file executable, then add it to ~/bin and to your path.

On Mac OS, move the executable to /usr/local/bin.

On Windows, move the executable to C:\Windows. 

## Usage:

### To get help info:

python3 dom_buster.py -h
    or
python3 dom_buster.py --help

### Run dom_buster on url (no xpath): 

python3 dom_buster --u=Your_Url_Path
    or
python3 dom_buster --url=Your_Url_Path
    or
python3 dom_buster --URL=Your_Url_Path

### Run dom_buster on url with xpath:

python3 dom_buster --u=Your_Url_Path --x=Your_Xpath
    or
python3 dom_buster --url=Your_Url_Path --xpath=Your_Xpath
    or
python3 dom_buster --URL=Your_Url_Path --XPATH=Your_Xpath


### Use Custom xss list (xpath flag also allowed with these calls)

python3 dom_buster --u=Your_Url_Path --l=res/path_to_xss_textfile
    or
python3 dom_buster --url=Your_Url_Path --list=res/path_to_xss_textfile
    or
python3 dom_buster --URL=Your_Url_Path --LIST=res/path_to_xss_textfile

### Parameters and Options: 

-h : help -description of program use, parameters, and options.
--url=, --u= : url parameter -Url path to the website to run the payload injection on.
--xpath=,--x= : [Optional] xpath parameter -Path to the element if input fields is embedded behind buttons or routing. Can be found by copying the xpath from the webpages source code in the browser's inspect tool.
--l, --list, --LIST : [Optional] custom xss list parameter: -Path to the text file that holds the custom xss calls you'd like to try on the input boxes

## Video on usage and purpose:

https://www.youtube.com/watch?v=JB-oG6SSUuM
