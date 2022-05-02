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
