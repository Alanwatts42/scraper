# Scraper Notes

<br>

### Notes associated to this project, and can't be comments in the actual code
---

<br>

## First Web Scraper tutorial
<a href='https://first-web-scraper.readthedocs.io/en/latest/'>https://first-web-scraper.readthedocs.io/en/latest/</a>

### 'First web scraper' github repository: <a href'http://www.github.com/ireapps/first-web-scraper/'>http://www.github.com/ireapps/first-web-scraper/</a>

This is a very good resource and model for how to put together a python web scraper
using beautifulsoup and requests.

Targets: 

1. https://romsmania.cc/  specifically: links <a href="www.links.com" class="places_links">links</a>



### Code snippets for each step of the process as shown in the tutorial
---

<br>


1. Retrieve and print html for a specific url

```
import requests

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
print(html)

```

<br>

2. Import the `BeautifulSoup` HTML parsing library and feed it the page
```
import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

```

<br>

3. Find what we need in the page's HTML and convert it into a simple, direct command that will instruct BeautifulSoup on how to extract only what we're after.


```
import requests
from bs4 import BeautifulSoup

url = http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'stripe'})
print(table.prettify())
```

<br>


4. Now that we have the table, we need to convert the rows of the table into a list, which we can loop through and grab the data from. 

We can do this by digging down into the table and returning a list of rows, which are created in HTML using <tr> tags inside the table. 

Basically, we can tell BeautifulSoup to find the <tr> tags, then return them as a list. This is done with a for loop: `for row in table.findAll('tr'):
    print(table.prettify())`


```
import requests
from bs4 import BeautifulSoup

url = http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'stripe'})

for row in table.findAll('tr'):
    print(table.prettify())
```




