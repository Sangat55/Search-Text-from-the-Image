from PIL import Image
import pytesseract
import argparse
import cv2
import os
from bs4 import BeautifulSoup
import urllib
import urllib.request
import copy

image = cv2.imread('image.png')
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray , 0 ,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray =  cv2.medianBlur(gray,3)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename,gray)
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
#
text = pytesseract.image_to_string(Image.open(filename), lang ='eng' ,config=tessdata_dir_config )
os.remove(filename)
query = copy.copy(text)
print(query)
def search(query):
    address = "http://www.bing.com/search?q=%s" % (urllib.parse.quote_plus(query))

    getRequest = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})

    urlfile = urllib.request.urlopen(getRequest)
    htmlResult = urlfile.read(200000)
    urlfile.close()

    soup = BeautifulSoup(htmlResult,'lxml')
    [s.extract() for s in soup('span')]
    results = soup.find_all('li', { "class" : "b_algo" })

    for result in results:
            print ("link: " + str(result.find('a' ).get('href')))
    unwantedTags = ['a' ,'strong', 'cite']
    for tag in unwantedTags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

        results = soup.find_all('li', { "class" : "b_algo" })
        for result in results:
            print ("# TITLE: " + str(result.find('h2')).replace(" ", " ") + "\n#")
            print ("# DESCRIPTION: " + str(result.find('p')).replace(" ", " "))
            print ("# ___________________________________________________________\n#")
    return results
search(query)


