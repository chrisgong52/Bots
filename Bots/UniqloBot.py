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
import string

shipping_page_info = {"First Name": "Chris",
                      "Last Name": "Gong",
                      "Street Address": "20341 Chateau Drive",
                      "Apartment or Unit # (Optional)": "",
                      "City": "Saratoga",
                      "Zip Code": "95070",
                      "Country": "United States",
                      "Phone Number": "4087979839",
                      }
account_info = {"Email":  "19christopherg@alumni.harker.org",
                "Password": "ChrisUniqlo315"
                }
payment_info = {"Email":  "19christopherg@alumni.harker.org",
                "Card Number": "4266 9020 5117 5436",
                "Month": "7",
                "Year": "2023",
                "CSV": "852",
                "Cardholder Name": "Chris Gong",
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

selections = driver.find_elements_by_class_name("attribute")
color_select = [selections[0]]
size_select = [selections[1]]
count = 0
color_to_select = "11 PINK"
size_to_select = "M"
color_select_link = ""
for item in color_select:
    print(item)
    color_list = item.find_element_by_class_name("value").find_element_by_tag_name("ul").find_elements_by_tag_name("li")
    for el in color_list:
#         print(el)
        temp = el.find_element_by_tag_name("a")
#         print(temp.get_attribute("title"))
#         print(temp.get_attribute("href"))
        if temp.get_attribute("title") == color_to_select:
            color_select_link = temp.get_attribute("href")
             
driver.get(color_select_link)

time.sleep(1)
selections = driver.find_elements_by_class_name("attribute")
size_select = [selections[1]]
size_select_link = ""
for item in size_select:
    size_list = item.find_element_by_class_name("value").find_element_by_tag_name("ul").find_elements_by_tag_name("li")
    for el in size_list:
#         print(el)
        temp = el.find_element_by_tag_name("a")
#         print(temp.get_attribute("title"))
#         print(temp.get_attribute("href"))
        if temp.get_attribute("title") == size_to_select:
            size_select_link = temp.get_attribute("href")
            
driver.get(size_select_link)

time.sleep(1)
driver.find_element_by_id("add-to-cart").click()
time.sleep(1)
checkout = driver.find_element_by_class_name("mini-cart-link-checkout")
checkout_link = checkout.get_attribute("href")
driver.get(checkout_link)

time.sleep(1)
inputs = driver.find_elements_by_tag_name("input")
for item in inputs:
    temp = item.get_attribute("class")
    if temp[0:10] == "input-text" and temp[11:24] == "usernameemail":
        email = item
    elif temp[0:10] == "input-text" and temp[11:19] == "password":
        password = item
    
email.send_keys(account_info["Email"])
password.send_keys(account_info["Password"])

driver.find_element_by_class_name("logincheckout").click()

time.sleep(2)

shipping_location = driver.find_element_by_id("delivery-store")
shipping_location.click()
time.sleep(2)

# field_wrappers = driver.find_elements_by_class_name("field-wrapper")
# print(field_wrappers)
print("clicked location")
zipcodes = driver.find_elements_by_class_name("input-text")
print("zipcodes: ", zipcodes)
for el in zipcodes:
    if el.get_attribute("id") == "dwfrm_storelocator_postalCode":
        print(el)
        zipcode = el
time.sleep(1)
zipcode.send_keys(shipping_page_info["Zip Code"])

search_zip = driver.find_element_by_name("dwfrm_storelocator_findbyzip")
search_zip.click()

time.sleep(1)

select = driver.find_element_by_class_name("select-store")
select.click()

time.sleep(1)

cont = driver.find_element_by_name("dwfrm_singleshipping_shippingAddress_save")
cont.click()

time.sleep(1)

def select_dropdown(el_id: string, look_up: dict, target: string):
    item = driver.find_element_by_id(el_id)
    for el in item.find_elements_by_tag_name('option'):
        if el.text == look_up[target]:
            el.click()
            
exit()
inputs = driver.find_elements_by_class_name("input-text")
sections = {}
for item in inputs:
    attr_id = item.get_attribute("id")
    if attr_id == "dwfrm_billing_paymentMethods_creditCard_owner":
        sections["Cardholder Name"] = item
    elif attr_id[0:46] == "dwfrm_billing_paymentMethods_creditCard_number":
        sections["Card Number"] = item
    elif attr_id[0:43] == "dwfrm_billing_paymentMethods_creditCard_cvn":
        sections["CSV"] = item
for item in sections.keys():
    sections[item].send_keys(payment_info[item])
    
dropdowns = driver.find_elements_by_class_name("list")
month = "asdfg"
print(type(month))
year = ""
print(dropdowns)
for el in dropdowns:
    temp = el.find_elements_by_class_name("option")
    if len(temp) == 13 and type(month) == str:
        print("assigning month")
        month = el
    elif len(temp) == 12:
        print("assigning year")
        year = el


lists = driver.find_elements_by_class_name("nice-select")
for el in lists:
#     try:
#     print(el.find_element_by_tag_name("ul"))
#     print(el.find_element_by_class_name("current").text)
    ddown = el.find_element_by_tag_name("ul")
#     print("getting el text: ", el.find_element_by_tag_name("ul").text)
    if el.find_element_by_class_name("current").text == "MONTH*":
        el.click()
        time.sleep(1)
        for item in ddown.find_elements_by_tag_name("li"):
#             print(item.get_attribute("data-value"))
            if item.get_attribute("data-value") == payment_info["Month"]:
                print("SENDING MONTH")
                item.click()
                time.sleep(1)
                lists = driver.find_elements_by_class_name("nice-select")
                break
        break
for el in lists:
    ddown = el.find_element_by_tag_name("ul")
    if el.find_element_by_class_name("current").text == "YEAR*":
        el.click()
        time.sleep(1)
        for item in ddown.find_elements_by_tag_name("li"):
#             print(item.get_attribute("data-value"))
            if item.get_attribute("data-value") == payment_info["Year"]:
                print("SENDING YEAR")
                item.click()
                break
        break
    
checkboxs = driver.find_elements_by_class_name("input-checkbox")
print(checkboxs)
checkboxs[1].click()
time.sleep(1)

cont = driver.find_element_by_class_name("button-fancy-large")
cont.click()

time.sleep(1)

buy = input("Input \"yes\" to purchase or \"no\" to quit: ")
if buy == "yes":
    purchase = driver.find_element_by_class_name("button-fancy-large")
    purchase.click()
else:
    driver.quit()
#                     el.find_element_by_class_name("current").text = item.text
#     except:
#         pass
# month_list = month.find_elements_by_tag_name("li")
# print(month_list)
# for el in month_list:
#     print(el.get_attribute("data-value"))
#     if el.get_attribute("data-value") == payment_info["Month"]:
#         el.click()
# year_list = year.find_elements_by_tag_name("li")
# print(year_list)
# for el in year_list:
#     print(el.get_attribute("data-value"))
#     if el.get_attribute("data-value") == payment_info["Year"]:
#         el.click()







