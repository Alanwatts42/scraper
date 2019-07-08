#/usr/bin/python3

import requests
from bs4 import BeautifulSoup
"""
Simple web page scraper: primarily utilitzing requests and bs4
"""

   
url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp" 

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, features="html.parser")

table = soup.find('tbody', attrs={'id': 'mrc_main_table'})

def get_table(tags="'tbody', attrs={'class': 'stripe'}"):
    """function for scraping data from a table on a webpage"""
    table = soup.find(tags)
    for row in table.findAll('tr'):
        return table.prettify()

if __name__ == '__main__':
    #get_table('tbody', {'class': 'stripe'})
    for row in table.findAll('tr'):
        print(table.prettify())


#### commeneted original code below - keeping for reference
#
# # url = input("What is the target url? ")
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
