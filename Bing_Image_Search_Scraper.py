"""
    REQUIREMENTS: Download "chromedriver" to C:\Drivers\ or to path specified in line 26
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import BeautifulSoup
from bs4 import BeautifulSoup
import lxml.html
import urllib
import urllib2
from urllib import FancyURLopener
import json
import re
from urllib2 import urlopen
import os
import sys
import urlparse
import io
import lxml.html
import urlparse
import posixpath
import requests

search = ''
path_to_chromedriver = 'C:\Drivers\chromedriver'    ####Change path! 


class MyOpener(FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()


def scrapeImage(url,name):
    #urlData = urllib2.urlopen(url)
    #bs = BeautifulSoup(urlData)

    if not os.path.exists("images/" + search):
        os.makedirs("images/" + search)

    #imgUrl = bs.find('img', attrs={'class': 'mainImage'}).get('src')
    
    urllib.urlretrieve(url, "images/" + search + "/" + name + ".jpg")
    print ""

def searchImgs(driver):
    scheight = .1
    while scheight < 9.9:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight += .01

    source = driver.page_source
    soup = BeautifulSoup(source)

    count = 0
    try:
        for img in soup.find_all('div', attrs={'class': 'dg_u'}):
            try:
                m = img.find('a').get('m')
                m = str(m)
            
                start = m.find('imgurl')
                start += 8
                end = m.find('.jpg') + 4
                imgURL = m[start:end]
                name = img.find('a').get('t1')
                scrapeImage(imgURL, name)
            except:
                print ""
    except:
        print "There were no public images available for " + search
    if(count == 0):
        print "There were no public images available for " + search
    else:
        driver.close()

def main():
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    driver.get("https://www.bing.com/images")
    #assert "Facebook" in driver.title
    elem = driver.find_element_by_id("sb_form_q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)
    searchImgs(driver)


if __name__ == "__main__":
    #Get username here
    search = raw_input("Enter search query: ")
    main()