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

payment_info = {"Email":  "19christopherg@alumni.harker.org",
                "Card Number": "4266 9020 5117 5436",
                "Month": "07 July",
                "Year": "2023",
                "CSV": "852",
                "Cardholder Name": "Chris Gong",
                }

PATH = "/Users/Maria/Desktop/Projects/Bots/chromedriver"

text_to_select = {"Black_high": "Men\'s 9.5",
                  "White_high": "Men\'s 9.5 / Women\'s 11.5"}

links_to_select = {"Black_high": "https://www.converse.com/shop/p/renew-chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170868C.html?dwvar_170868C_color=black%2Fmason%2Fwhite&styleNo=170868C&cgid=mens-shoes",
                   "White_high": "https://www.converse.com/shop/p/chuck-taylor-all-star-crater-knit-unisex-high-top-shoe/170368MP.html?pid=170368MP&dwvar_170368MP_color=white%2Fegret%2Fbarely%20volt&dwvar_170368MP_width=standard&styleNo=170368C&pdp=true"}

'''
    id is the id of the element we want to find by id
    look_up is the dictionary to look up the value you want from
    target is the target value in the look_up dictionary
    ex: pass in payment_info with 
'''
def select_dropdown(el_id: string, look_up: dict, target: string):
    item = driver.find_element_by_id(el_id)
    for el in item.find_elements_by_tag_name('option'):
        if el.text == look_up[target]:
            el.click()
            
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
# print(boxes)
for item in boxes:
    try:
        label = item.find_element_by_class_name("field__label").text
#         print(label)
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
#             print("jkhgfdfghjk")
            checkbox = item.find_element_by_class_name("field__label--checkbox")
#             print("djklsjkljgklfjkljfklgjflkgjdkljflkfjkljf")
#             print("checkbox: ", checkbox)
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
# time.sleep(1)
# email_uncheck = driver.find_element_by_id("dwfrm_billing_billingAddress_addToEmailList")
# email_uncheck.click()
# test = driver.find_elements_by_class_name("field-wrapper")
# for element in test:
#     a = element.find_element_by_class_name("input-choice")
#     a.click()

email = driver.find_element_by_id("dwfrm_billing_billingAddress_email_emailAddress")
email.send_keys(payment_info["Email"])

credit_card = driver.find_element_by_class_name("payment-method__label")
credit_card.click()

time.sleep(1)
card_number = driver.find_element_by_id("creditCard_number")
card_number.send_keys(payment_info["Card Number"])

# month = driver.find_element_by_id("creditCard_expiration_month")
# for el in month.find_elements_by_tag_name('option'):
#     if el.text == payment_info["Month"]:
#         el.click()
select_dropdown("creditCard_expiration_month", payment_info, "Month")
select_dropdown("creditCard_expiration_year", payment_info, "Year")
csv = driver.find_element_by_class_name("validate-cvv")
csv.send_keys(payment_info["CSV"])

cardholder_name = driver.find_element_by_id("creditCard_owner")
cardholder_name.send_keys(payment_info["Cardholder Name"])

time.sleep(1)

billing_submit = driver.find_element_by_id("billing-submit")
billing_submit.click()



# month = driver.find_element_by_id("creditCard_expiration_month")
# for el in month.find_elements_by_tag_name('option'):
#     if el.text == payment_info["Month"]:
#         el.click()



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