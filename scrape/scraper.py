#/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import lxml

"""
Simple web page scraper: primarily utilitzing requests and bs4

url="https://stackoverflow.com/questions/57200316\
/use-self-type-as-return-type-in-scala-trait\
/57200887#57200887"
"""

class get:

    url = input("enter url: ") 
    if url is not 
    result = requests.get(url)
    html = result.content
    soup = BeautifulSoup(html, lxml)

    # def grandFather(info):    
    #     family = soup.findAll(text=info)[0].parent
    #     return family

    def search(tag):
        result = soup.findAll(text=tag)
        print(result)

if __name__ == '__main__':
    get()
    t = input("enter tag to search: ")
    search(t)
    
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
