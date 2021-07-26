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
driver.get("https://www.adidas.com/us/stan-smith-shoes/FX5500.html")

buttons = driver.find_elements_by_css_selector("button")
for item in buttons:
    try:
        if item.find_element_by_css_selector("span").text == "10":
            print("clicking")
            time.sleep(1)
            item.click()
        if item.find_element_by_css_selector("span").text == "Add To Bag":
            time.sleep(3)
            print("clicking add to bag")
            item.click()
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        pass