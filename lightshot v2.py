# Lightshot screen-shot web scraper, generates random screen-shot url and saves the picture
# need the beautifulscraper library to work

from random import *
import time
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

word = ""
final = []
numPages = 100

for i in range(0, numPages):

    print("Num: ", i + 1)

    for x in range(0, 3):
        word += (choice(letters))
        word += (choice(numbers))

    w = list(word)
    shuffle(w)
    word = ''.join(w)

    url = "https://prnt.sc/" + word
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src': re.compile('.jpg')})
    images2 = bs.find_all('img', {'src': re.compile('.png')})

    for img in images:
        if img['alt'] == 'Lightshot screenshot':
            # print(img2['src'] + '\n')
            try:
                urllib.request.urlretrieve(img['src'], 'img4/' + word + '.jpg')
                print(img['src'])
            except urllib.error.HTTPError:
                print("urllib.error.HTTPError: HTTP Error 403: Forbidden")
                time.sleep(2)


    for img2 in images2: # Img url for the missing image has to be updated, they change the exact url every once in awhile,just inpsect element to get
        if img2['alt'] == 'Lightshot screenshot' and img2['src'] != '//st.prntscr.com/2020/08/01/0537/img/0_173a7b_211be8ff.png':
            # print (img2)
            # print(img2['src'] + '\n')
            try:
                urllib.request.urlretrieve(img2['src'], 'img4/' + word + '.png')
                print(img2['src'])
            except urllib.error.HTTPError:
                print("urllib.error.HTTPError: HTTP Error 403: Forbidden")
                time.sleep(2)

    time.sleep(2)
    word = ""


print("Done.")