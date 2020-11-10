#! python3
# downloadXKCD.py - Downloads EVERY single XKCD comic!

import requests, os, bs4

comicUrl = ''
url = 'https://xkcd.com'     # Starting url
os.makedirs('xkcd', exist_ok=True)  #Store comics in ./xkcd/comics
while not url.endswith('#'):
  # Download the page
  print('Downloading page %s...' % url)
  res = requests.get(url)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text)

  # Find the URL of the comic image
  comicElem = soup.select('#comic img')
  if (comicElem == []):
    print('Could not find the comic image.')
  else:
    comicUrl = 'https:' + comicElem[0].get('src')
    # Download the image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Save the image file to ./xkcd
    with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
      for chunk in res.iter_content(100000):
        imageFile.write(chunk)

  # Get the Prev button's url
  prevLink = soup.select('a[rel="prev", accesskey="p"]')[0]
  url = 'https://xkcd.com' + prevLink.get("href")
# TODO: Download the page.
# TODO: Find the url of the comic image
# TODO: Save the image to ./xkcd
# TODO: Get the Prev button's url.

print('Done.')


