'''
Created on May 19, 2021

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
import string

PATH = "/Users/Maria/Desktop/Projects/Bots/chromedriver"

login_info = {"username": "gongc7", "password": "Mvvclub25!"}
# classes = ["35750", "35751", "35754"]
classes = ["34160", "34165"]

driver = webdriver.Chrome(PATH)
driver.get("https://webreg2.reg.uci.edu/cgi-bin/wramia?page=login?call=0041")
access_button = driver.find_element_by_name("button")
access_button.click()
time.sleep(1)
username = driver.find_element_by_name("ucinetid")
username.send_keys(login_info["username"])
password = driver.find_element_by_name("password")
password.send_keys(login_info["password"])
login = driver.find_element_by_name("login_button")
login.click()
time.sleep(1)
buttons = driver.find_element_by_class_name("vertButtons")
for item in buttons.find_elements_by_tag_name("form"):
    print(item)
    el = item.find_element_by_class_name("WebRegButton")
    el.click()
    break
time.sleep(1)

for item in classes:
    code = driver.find_element_by_name("courseCode")
    code.send_keys(item)
    add = driver.find_element_by_id("add")
    add.click()
    drop = driver.find_element_by_id("drop")
    change = driver.find_element_by_id("change")
    grade = driver.find_element_by_name("gradeOption")
    grade.send_keys("1")
    submit = driver.find_element_by_name("button")
    submit.click()
    time.sleep(1)

'''
code = driver.find_element_by_name("courseCode")
code.send_keys(classes[0])
add = driver.find_element_by_id("add")
add.click()
drop = driver.find_element_by_id("drop")
change = driver.find_element_by_id("change")
grade = driver.find_element_by_name("gradeOption")
grade.send_keys("1")
# inputs = driver.find_elements_by_tag_name("input")
submit = driver.find_element_by_name("button")
submit.click()
'''


# print(inputs)
# for item in inputs:
#     try:
#         print(item.name)
#     except AttributeError
    

# enrollment_button = driver.find_element_by_class_name("WebRegButton")
# enrollment_button.click()