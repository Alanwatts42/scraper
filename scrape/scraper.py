#!/usr/bin/python3

from validators import url
import requests
from bs4 import BeautifulSoup
import lxml

"""
Simple web page scraper: primarily utilitzing requests and bs4

url="https://stackoverflow.com/questions/57200316\
/use-self-type-as-return-type-in-scala-trait\
/57200887#57200887"
"""

class stew:

    def check_url(site):
        r = url(site)
        return r

   
    
    site = input("enter url: ")
    while check_url(site) is not True:
        try:
            check_url(site)
            break
        except valueerror:
            print("url is not valid, please try again.")
    
    print("url validation for " + site + "successful!")



    # def grandFather(info):    
    #     g = soup.findAll(text=info)[0].parent
    #     return g


class ladle:

    result = requests.get(site)
    html = result.content
    soup = BeautifulSoup(html, features='html.parser')
    
    def search(tag):
        result = soup.findAll(text=tag)
        print(result)
    
    t = input("enter tag to search: ")
    
    search(t)



if __name__ == '__main__':
    stew()
    ladle()

#### commented original code below - keeping for reference
#
# table = soup.find('tbody', attrs={'id': 'mrc_main_table'})
# url = input("What is the target url? ")
# url = 'https://romsmania.cc/'
#
# result = requests.get(url)
# html = result.content
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
