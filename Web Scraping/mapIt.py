# mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser
import sys
import pyperclip

if not pyperclip.is_available():
  print("Copy functionality unavailable, please install the pyperclip package")
  exit

if(len(sys.argv) > 1):
  #Get the address from the command line
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)