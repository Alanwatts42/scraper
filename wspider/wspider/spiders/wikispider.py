#!/bin/python3

import scrapy as s

class firstspider(s.Spider):
    name = "wikis"
    
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Application_programming_interface', 
            'https://en.wikipedia.org/wiki/Calling_convention'
        ]
        for url in urls:
            yield s.Request(url=url, callback=self.parse)

    def parse(self, response):
        article = response.url.split("/")[-1]
        filename = 'wikis-%s.html' % article
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


