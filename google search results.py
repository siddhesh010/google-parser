"""


@author: SIDDHESH NAIK
"""

#DOWNLOAD chromedriver.exe ACCORDING TO UR VERSION OF CHROME
#SET executable_path TO THE FILE LOCATION OF chromedriver.exe
#DESIGNED TO FIND THE LINK TO FIRST GOOGLE SEARCH
#FindAll ATTRIBUTE CAN BE USED TO FIND LINKS OF ALL GOOGLE SEARCHES


from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests


input_=input("ENTER YOUR SEARCH:\n")
url = 'https://google.com/search?q={}'.format(input_)
driver = webdriver.Chrome(executable_path="G://chromedriver.exe")
driver.get(url)
html = bs(driver.page_source, "lxml")
driver.quit()
div = html.find('div', {'class': 'g'})
link=div.a.get("href")
print(link)
