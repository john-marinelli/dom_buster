from bs4 import BeautifulSoup
import requests

request = requests.get("https://stackoverflow.com/questions/8936030/using-beautifulsoup-to-search-html-for-string")


soup = BeautifulSoup(request.text, 'html.parser')
i =0

for element in soup.find_all():
    print(element)
    i += 1
    print(i)


