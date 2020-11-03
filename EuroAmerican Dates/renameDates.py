import os
import pathlib
import shutil
from pathlib import Path
import zipfile
import re

def convDate(unknown):
  amerDate = re.compile(r'([0-1\d])-([[0-3^4-9]0-9])-([1-2\d{3}])', re.I)
  query = amerDate.search(unknown)
  if(query is not type(None)):
    amerDate.sub(r"group(2)-group(1)-group(3)")

def dirScout(fun):
  Path.resolve(fun)
  dirName, subDir, fileNames = Path.iter_dir(fun)
  for directory in enumerate(dirname):
    
    for subDirectory in enumerate(subDir):
      for i in len(fileNames):
        convDate(fileNames[i])
  



"""
Function Skeletons:

1: Function to walk the directory Tree
2: Function to loop through the subdirectories (Use List Comprehension)
3: Function to loop through the files (Use List Comprehension + convDate)
"""