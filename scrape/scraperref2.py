#/usr/bin/python3

"""
# Webscraper Reference 2
"""

import requests
from bs4 import BeautifulSoup

"""
## Target 

### Website: 
https://www.whitehouse.gov/briefings-statements

### Data: 
Records of 
presidential briefings
and statements.

### Goal: 
Extract all links on page for briefings and statements
"""

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)

