# Scraper

<br>

## Evan Sherwood

<a href='https://github.com/Alanwatts42/scraper'> https://github.com/Alanwatts42/scraper</a>

### "It is what it is..."  - god, after a week of failed attempts, settling for what he ended up with.

<br>

This is a very..  VERY.. Simple web scraper written in Python 3, and utilizing the Requests and Beautiful Soup 4 libraries.

<br>

Don't expect much out of this. The primary purpose of this project is 
for my own benefit. It's a practice-run, an old beater car driven by a kid 
who just got their license, that first high school "relationship" that 
everyone knows isn't going to last but is nevertheless a necessary 
milestone that needs to happen, awkwardness not withstanding.

<br>

### Details that are useful to me (and possibly only to me, but here they are anyway)
---
- I am using `pipenv` for virtual environment and dependency management. Why? Because it makes more sense to me than virtualenv ever did.
- The structure of this project is what I believe to be the typical structure of a python project. Top level directory will contain the README.md and the LICENSE. There's a directory for the primary script(s) called scraper, and a folder for tests. If I end up using any other files that don't fall into either of these two categories, I'll have a directory for those as well, whatever they may be.
- The scraper will use `requests` to pull the required web pages, and `beautifulsoup` to parse through the html/css/js of said web pages to find the info or files being scraped.
- I will be attempting an object-oriented approach, and despite a middling understanding of classes in general, will do the best I can to implement them.
- The initial goal is to create a general tool that can be used to scrape a variety of info. Whether or not this is what I end up with, that's what I'll be shooting for. I might end up needing to narrow the scope to scraping just text info, let's say, but ideally I will attempt to make a tool that can scrape files, pictures, or text, from the same interface.
- The UI will almost certainly be command-line based. I have enough experience to know the pitfalls of a GUI, and I don't want to bite off more than I can chew.
- I will probably use something like `argparse` to implement simple command line arguments that can adjust some simple settings for what is being scraped or how the results are being parsed or output to the user.
- If the gods are with me, perhaps I will succeed in this endeavor. May the force be with me, and may the hair on my toes never fall out. May the odds be ever in my.... no that's going too far. Excelsiar!
