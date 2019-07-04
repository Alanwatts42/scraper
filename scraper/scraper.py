#/usr/bin/python3

from bs4 import BeautifulSoup
import requests
"""

"""



# url = input("What is the target url? ")
url = 'https://romsmania.cc/'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, features='html.parser')
links = soup.find('ul', attrs={'class': 'dropdown__list'})


if __name__ == '__main__':
    
    for link in links.findAll('li'):
        print(links.prettify())


