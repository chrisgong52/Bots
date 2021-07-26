'''
Created on Jun 23, 2021

@author: Maria
'''

'''
Created on Jun 15, 2021

@author: Maria
'''
from purpleair.network import SensorList
from flask import Flask, render_template, request, redirect, jsonify, make_response
import requests
import pprint
import operator as op
from functools import reduce
import math
import json
import itertools
import datetime
import time
import hashlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import string

PATH = "/Users/Maria/Desktop/Projects/Bots/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://disneyworld.disney.go.com/admission/tickets/")

# time.sleep(3)
buttons = driver.find_elements_by_css_selector("button")
b = driver.find_elements_by_css_selector("a")
print(b)
for item in b:
    print(item.get_attribute("class"))
    try:
        print("HREF: ", item.get_attribute("href"))
        item.click()
    except:
        pass

print(buttons)
for item in buttons:
#     print(type(item))
    try:
        print("id: ", item.get_attribute("id"))
    except:
        print("no id")
        
time.sleep(3)        

inputs = driver.find_elements_by_css_selector("input")
for item in inputs:
    print(item)