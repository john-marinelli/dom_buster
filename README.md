# Dom Buster

## Overview:

Dom Buster is a tool used for testing websites for cross-site scripting vulnerabilities,\ 
with a particular emphasis on those having to do with the Document Object Model.\

It's a dynamic analysis tool that treats a website as a black box, simulating repeated\
cross-site scripting attempts and reporting back vulnerabilities.\

Dom Buster does not require any access to your code base.\

## Installation:

Dom Buster uses Selenium and chromedriver to search and interact with webpages. In order to\
start using the program, you must install both of these.\

#To install Selenium:

```

pip3 install selenium

```

#To install chromedriver:

On Windows, we recommend using Chocolatey, a package manager:

```

choco install chromedriver

```


On Mac OS, we recommend using Homebrew:

```

brew --cask install chromedriver

```

On Linux, you may find chromedriver on many major package managers:



