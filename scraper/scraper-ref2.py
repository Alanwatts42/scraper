#/usr/bin/python3

# Webscraper Reference 2

# Obtaining links from website: 
# https://www.whitehouse.gov/briefings-statements

# One of the things on this website is records of presidential briefings
# and statements.

# Goal: Extract all links on page for briefings and statements

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)


