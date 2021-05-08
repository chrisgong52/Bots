'''
Created on May 7, 2021

@author: Maria
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import time

PATH = "/Users/Maria/Desktop/Projects/Bots/chromedriver"
button_vals = []
driver = webdriver.Chrome(PATH)

driver.get("https://www.converse.com/shop/p/renew-chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170868C.html?dwvar_170868C_color=black%2Fmason%2Fwhite&styleNo=170868C&cgid=mens-shoes")
button_vals = []
ops = driver.find_element_by_id('variationDropdown-size')
drop_down = driver.find_element_by_id('variationDropdown-size')
out = [x for x in drop_down.find_elements_by_tag_name("option")]


d_down = driver.find_element_by_xpath("//select[@id='variationDropdown-size']")
for el in d_down.find_elements_by_tag_name('option'):
    if el.text == "Men\'s 10":
        el.click()

time.sleep(1)

temp = driver.find_element_by_xpath('//button[text()="Add to Cart"]')
# print(temp)
temp.submit()

time.sleep(1)
driver.find_element_by_name('dwfrm_cart_checkoutCart').click()


'''
options = []
ops_dict = {}
for element in out:
#     print(element.get_attribute("value"), element.get_attribute("data-label"))
    size = json.loads(element.get_attribute("data-label"))
    print(size)
    options.append((json.loads(element.get_attribute("data-label")), element.get_attribute("value")))
    if size['key'] == 'Size':
        ops_dict[size['value']] = element.get_attribute("value")
    
    
for item in options:
    print(item)
    print(type(item[0]))
'''
# ops.send_keys('Men\'s 10')
# # driver.find_element_by_class_name('button button--primary button--add-to-cart-pdp set--full set--themeable')
# temp = driver.find_element_by_xpath('//button[text()="Add to Cart"]')
# # print(temp)
# temp.submit()
# 
# # driver.find_element_by_css_selector(".button--primary").click()
# 
# # driver.get("https://www.converse.com/shop-cart")
# print("lsdkjflksdjf")