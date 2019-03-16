from PIL import Image
import pytesseract
import cv2
import os
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
"""
filename = 'image.jpg'
im = Image.open(filename)          //Convert into .png file

im.save('image.png')
"""
name = 'image.png'

text = pytesseract.image_to_string(Image.open(name), lang ='eng' ,config=tessdata_dir_config )


unwanted = ";'.></\=-"
for char in unwanted:
    text = text.replace(char,"")
print(text)
text = str(text)
def searchOnnet(text):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome('E:/chromedriver')
    driver.get("https://www.duckduckgo.com/?q=%s" % (urllib.parse.quote_plus(text)))
    urls = driver.find_elements_by_css_selector(".result__url.js-result-extras-url")
    for url in urls:
        print(url.text)
       
searchOnnet(text)