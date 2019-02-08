from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url="https://www.gigantti.fi/catalog/tietokoneet/fi_kannettavat/kannettavat-tietokoneet"

browser = webdriver.Chrome()

# Tell selenium to go to url
browser.get(url)

page_length = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
match = False
while (match == False):
    lastCount = page_length
    time.sleep(3)
    page_length = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
    if lastCount == page_length:
        match=True

source_data = browser.page_source

with open("gigantti_laptop.html", "w") as file:
    file.write(source_data)

print("Done !")
