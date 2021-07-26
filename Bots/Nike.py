'''
Created on Jul 26, 2021

@author: Maria
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from plyer import notification

shipping_page_info = {"First Name": "Chris",
                      "Last Name": "Gong",
                      "Street Address": "20341 Chateau Drive",
                      "Apartment or Unit # (Optional)": "",
                      "City": "Saratoga",
                      "Zip Code": "95070",
                      "Country": "United States",
                      "Phone Number": "4087979839",
                      }
