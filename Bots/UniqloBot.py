'''
Created on May 11, 2021

@author: Maria
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException

shipping_page_info = {"First Name": "Chris",
                      "Last Name": "Gong",
                      "Street Address": "20341 Chateau Drive",
                      "Apartment or Unit # (Optional)": "",
                      "City": "Saratoga",
                      "Zip Code": "95070",
                      "Country": "United States",
                      "Phone Number": "4087979839",
                      }

PATH = "/Users/Maria/Desktop/Projects/Bots/chromedriver"

text_to_select = {}

links_to_select = {"salmon hoodie": "https://www.uniqlo.com/us/en/men/sweatshirts-and-sweatpants"}
button_vals = []
driver = webdriver.Chrome(PATH)

purchase_item = "ITEM TO PURCHASE HERE FOR KEY TO TEXT TO SELECT AND LINKS TO SELECT"

driver.get("https://www.uniqlo.com/us/en/men/sweatshirts-and-sweatpants")
print("lsdkjfslkdf")
hoodie = driver.find_element_by_id("393f2a0cf4ade35894724c08a9")
a = hoodie.find_element_by_class_name("product-tile-info")
b = a.find_element_by_class_name("product-img-swatches-info")
c = b.find_element_by_class_name("hover-wrapper")
d = c.find_element_by_class_name("product-image")
e = d.find_element_by_class_name("thumb-link")
print(e.get_attribute("href"))
link_to_product = e.get_attribute("href")
driver.get(link_to_product)
# e = d.find_element_by_xpath('//a[@href="'+url+'"]')