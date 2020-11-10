#! python3
# meetings.py - Selects for the meetings from the WNCNA website.

import requests, sys, webbrowser, bs4, lxml, re
from bs4 import SoupStrainer

# Display text while downloading the meetings page
print('Searching...')
aTags = SoupStrainer("a")
# meeting = requests.get('https://wncna.org/meetings' + ' '.join(sys.argv[1:]))
url="https://wncna.org/meetings/"
html_content = requests.get(url).text
html_content.raise_for_status()

# TODO: Retrieve meeting links

# meeting.find_all(href=re.compile("zoom"))
# Retrieve the meeting links
meetings = bs4.BeautifulSoup(html_content, "lxml", parseOnlyThese=SoupStrainer('table', 'bmlt-column3'))
links = meetings .findAll('a')
for link in links:
  print("Inner Text: {}".format(link.text))
  print("Title: {}".format(link.get("title")))
  print("href: {}".format(link.get("href")))
  print("meetings: {}".format(link.find_all(("zoom"))))
# Open a browser tab for each result.
# i = list()
linkElems = meetings.select('div:nth-child(i) > a')
numOpen = max(linkElems,5)
#meeting-data-row-6736 > td.bmlt-column3 > div:nth-child(2) > a

#meeting-data-row-6836 > td.bmlt-column3 > div:nth-child(3) > a

# TODO: Open each resulting meeting

