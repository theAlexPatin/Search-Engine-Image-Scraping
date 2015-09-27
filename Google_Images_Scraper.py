__author__ = 'apatin'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib
import os
path_to_chromedriver = 'C:\Drivers\chromedriver'    ####Change path!

sQuery = ''



def scroll(driver):
    driver.implicitly_wait(100)
    scheight = .1
    while scheight < 9.9:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        scheight += .01

def downloadImage(imgUrl):
    filename = imgUrl.split('/')[-1]	#Gets the name of the image
    try:
        if not os.path.exists("images"):
            os.makedirs("images")
        urllib.urlretrieve(imgUrl, "images/" + filename)	#Downloads the image to specified path
    except:
        print""

def findImages(driver):
    source = driver.page_source		#Gets the source of the page
    soup = BeautifulSoup(source)	#Parses the source
    driver.close()	
    try:
        for img in soup.find_all('a', attrs={'class': 'rg_l'}):		#Finds all "a" tags with the "rg_l" class
            url = img.get('href')		#Gets the image url
            i = url.find("imgurl=")		#This all parses out the useable portion of the image url
            i += 7						#
            j = i                       # (I didn't know about that whole string.split() nonsense but this achieves the same thing)
            while url[j] != "&":        # So excuse this section of code
                j += 1                  #
            downloadImage(url[i:j])     #
    except:
        print "There were no images available"

def main():
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    driver.get("https://www.google.com/images")
    elem = driver.find_element_by_id("lst-ib")	#Finds the search box (has this id tag)
    elem.send_keys(sQuery)
    elem.send_keys(Keys.RETURN)
    scroll(driver)	#Dynamically loads images
    findImages(driver)


if __name__ == "__main__":
    sQuery = raw_input("Please enter search query: "
    main()

