#/usr/bin/python3

import requests
from bs4 import BeautifulSoup

# Setting url default to google.com homepage if no other url is given
url = "https://www.google.com"

# Variable 'result' holds the data retrieved by requests.get(url)
result = requests.get(url)


""" 
To make sure site is accessible, printing the http status code of 
the requests.get(url) function call aka our 'result' variable. 
This should print something like 200 or even wifi is off it will 
print 404 code for not found. However, if our python code is wrong,
result will be None and no http result code will print. 
"""
print(result.status_code) 

""""
We can also check the HTTP header of the website to verify 
we have accessed correct page. See url below for reference 
on HTTP status codes.

https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
"""
print(result.headers) 
 
""" 
Now let's store the page content of the website accessed from 
requests to a variable
"""
src = result.content

"""
Now that we have the page source stored, we will use the 
BeautifulSoup module to parse and process the source. To do so, 
we create a BeautifulSoup object based on the source variables we 
created above:
"""
soup = BeautifulSoup(src, 'lxml')

"""
# Now that page source has been processed via BeautifulSoup we 
can access specific information directly from it. For instance, 
say we want a list of all the links on the page:
"""
links = soup.find_all("a")
print(links)
print("\n")

for link in links:
    if "Maps" in link.text:
        print(link)
        print(link.attrs['href'])


