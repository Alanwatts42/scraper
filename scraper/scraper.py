#usr/bin/python3

import requests
from bs4 import BeautifulSoup
"""
Simple web page scraper: primarily utilitzing requests and bs4
"""
   
url="https://stackoverflow.com/questions/57200316/use-self-type-as-return-type-in-scala-trait/57200887#57200887"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, features="html.parser")


def grandFather(info):    
    """info var is a unique data point within the target data, easily searched.
    function returns all of its parent data, making it easier to know
    what to scrape"""
    family = soup.findAll(info)[0].parent.parent
    return family

       

if __name__ == '__main__':
    d = grandFather("ConcreteType=")
    print('d')




#### commented original code below - keeping for reference
#
# table = soup.find('tbody', attrs={'id': 'mrc_main_table'})
# url = input("What is the target url? ")
# url = 'https://romsmania.cc/'
#
# response = requests.get(url)
# html = response.content
#
# soup = BeautifulSoup(html, features='html.parser')
# links = soup.find('ul', attrs={'class': 'dropdown__list'})
#
#
# if __name__ == '__main__':
#     
#     for link in links.findAll('li'):
#         print(links.prettify())
#
#
