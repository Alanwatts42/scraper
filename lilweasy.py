#!/usr/bin/python3

from WeasyPrint import HTML

url = 'https://realpython.com/python-thinking-recursively/'

article = url.split("/")[-1]
hurl = HTML(url)
hurl.write_pdf('/home/evan/_projects/scraper/transmute/' + article)




