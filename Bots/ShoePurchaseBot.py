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
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

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

text_to_select = {"Black_high": "Men\'s 10",
                  "White_high": "Men\'s 10 / Women\'s 12"}

links_to_select = {"Black_high": "https://www.converse.com/shop/p/renew-chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170868C.html?dwvar_170868C_color=black%2Fmason%2Fwhite&styleNo=170868C&cgid=mens-shoes",
                   "White_high": "https://www.converse.com/shop/p/chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170368MP.html?pid=170368MP&dwvar_170368MP_color=white%2Fegret%2Fbarely%20volt&dwvar_170368MP_width=standard&styleNo=170368C&pdp=true"}
button_vals = []
driver = webdriver.Chrome(PATH)

Shoes_to_buy = "White_high"

# driver.get("https://www.converse.com/shop/p/renew-chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170868C.html?dwvar_170868C_color=black%2Fmason%2Fwhite&styleNo=170868C&cgid=mens-shoes")
# driver.get("https://www.converse.com/shop/p/chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170368MP.html?pid=170368MP&dwvar_170368MP_color=white%2Fegret%2Fbarely%20volt&dwvar_170368MP_width=standard&styleNo=170368C&pdp=true")
driver.get(links_to_select[Shoes_to_buy])
button_vals = []
ops = driver.find_element_by_id('variationDropdown-size')
drop_down = driver.find_element_by_id('variationDropdown-size')
out = [x for x in drop_down.find_elements_by_tag_name("option")]


d_down = driver.find_element_by_xpath("//select[@id='variationDropdown-size']")
for el in d_down.find_elements_by_tag_name('option'):
    if el.text == text_to_select[Shoes_to_buy]:
        el.click()

time.sleep(1)

temp = driver.find_element_by_xpath('//button[text()="Add to Cart"]')
# print(temp)
temp.submit()

time.sleep(1)
driver.find_element_by_name('dwfrm_cart_checkoutCart').click()

boxes = driver.find_elements_by_class_name("field-wrapper")
print(boxes)
for item in boxes:
    try:
        label = item.find_element_by_class_name("field__label").text
        print(label)
        if label in shipping_page_info.keys():
            submit_box = item.find_element_by_class_name("input-text")
            submit_box.send_keys(shipping_page_info[label])
        elif label == "State":
            select_box = item.find_element_by_class_name("input-select")
            for item in select_box.find_elements_by_tag_name("option"):
                if item.text == "California":
                    item.click()
                    break
#             d_down = driver.find_element_by_xpath("//select[@id='variationDropdown-size']/option[text()='California']").click()
#             selection = select_box.find_element_by_xpath("/option[text()='California'").click()
#             print("selection: ", selection)
        elif label == "My billing address is the same.":
            print("jkhgfdfghjk")
            checkbox = item.find_element_by_class_name("field__label--checkbox")
            print("djklsjkljgklfjkljfklgjflkgjdkljflkfjkljf")
            print("checkbox: ", checkbox)
            checkbox.click()
        else:
            print("not in keys")
    except NoSuchElementException:
        print("No such element exception")
    except StaleElementReferenceException:
        print("Stale Element Exception")
        
driver.find_element_by_id("shipping-submit").click()
time.sleep(1)
driver.find_element_by_class_name("address-recomm").click()
driver.find_element_by_class_name("address-verification__continue").click()





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