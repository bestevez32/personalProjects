# This is a work in progress...


import requests

from bs4 import BeautifulSoup

def variable_spider(max_pages):
    page = 1
    while page <= max_pages:
        url='page url, leave page = blank' + str(page)
        source_code = requests.get(url)
        # Connects to a web page and stores values in a variable called source_code.

        plain_text = source_code.text
        # Takes text of the url request and stores it in a variable called plain_text

        soup = BeautifulSoup(plain_text)
        # Converts the web page information into a Beautiful Soup object, the data must be formatted
        # before bs4 can read it.

        for link in soup.findAll('a', {'class':'item-name'}):

        # This goes through source code.
        # Finds All of a specific item. 'a' are links(anchors)in HTML.
        # { : } are based on an attribute and value in source code on web page.

        href = "main page url" + link.get('href')
        # this will provide a link to each appropriate page in the url.

        title = link.string
        # This will provide the string title of each item on the page, otherwise all you would have is a link
        # with no description.

        print(href)
        print(title)
        page += 1


