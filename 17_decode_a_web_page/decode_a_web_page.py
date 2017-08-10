import requests
from bs4 import BeautifulSoup
import os, errno

url = 'http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html'
print(url)
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.title.string
title = title.lower()
title = title.replace(" ", "_")
print (title)
path = ("/home/jan/Repos/practice-python/" + title)
print(path)
try:
    os.makedirs(path)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise    
