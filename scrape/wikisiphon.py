# Example 3 - Scraping content and outputting result to a file

import requests
from bs4 import BeautifulSoup


page_url = requests.get(
    'https://en.wikipedia.org/List_of_Asian_countries_by_area'
).text

soup = BeautifulSoup(page_url, 'lxml')

print(soup.prettify())

