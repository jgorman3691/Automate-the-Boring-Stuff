#! python3
# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4, lxml

print('Googling...') # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(html_doc, 'lxml')
# Open a browser tab for each result.
linkElems = soup.select('div.yuRUbf a')
numOpen = min(5, len(linkElems))
print(list(linkElems))
for i in range(numOpen):
  webbrowser.open('https://google.com' + linkElems[i].get('href'))

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result