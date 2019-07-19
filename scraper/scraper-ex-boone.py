#usr/bin/python3

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
    # Loop over html to find and show the content contained within all instances    
    # of a specific html tag
    #get_table('tbody', {'class': 'stripe'})
    for row in table.findAll('tr'):
        print(table.prettify())
