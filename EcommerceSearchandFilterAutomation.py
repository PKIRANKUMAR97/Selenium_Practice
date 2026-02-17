# 3. Search + Filter Automation (E-commerce);
# Task: Open shopping site;
# Search product;
# Apply filters (price/brand);
# Add to cart;
# Verify cart

import os
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.snapdeal.com/")
search_txt = driver.find_element(By.ID,"search-box-input")
search_txt.send_keys("shoes for men")
search_txt.send_keys(Keys.ENTER)
mywait=WebDriverWait(driver,10)
action=ActionChains(driver)

slider_min_price = driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")

slider_max_price = driver.find_element(By.XPATH,"//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")

# print(slider_min_price.location, slider_max_price.location) # {'x': 70, 'y': 366} {'x': 257, 'y': 366}

action.drag_and_drop_by_offset(slider_max_price,-50,0)
action.perform()
action.drag_and_drop_by_offset(slider_min_price,+50,0)
action.perform()
time.sleep(5)
# slider_min_price_new = driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
#
# slider_max_price_new = driver.find_element(By.XPATH,"//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
# print(slider_min_price_new.location, slider_max_price_new.location)
brand=driver.find_element(By.XPATH,"//div[@data-filtername='Brand']//i[@class='sd-icon sd-icon-plus']")
brand.click()
time.sleep(3)
driver.find_element(By.XPATH,"//label[@for='Brand-Aadi']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"a[class='dp-widget-link noUdLine hashAdded'] p[title='Aadi Lifestyle Green Casual Shoes']").click()

window=driver.window_handles[1]
driver.switch_to.window(window)

driver.find_element(By.XPATH,"//span[normalize-space()='add to cart']").click()
driver.find_element(By.XPATH,"//div[normalize-space()='View Cart']").click()


cart_product=driver.find_element(By.XPATH,"//a[@title='Aadi Lifestyle Khaki Casual Shoes']").text
print(cart_product)
assert "Aadi" in cart_product
print(" succesfulyy added in cart ")

driver.close()

time.sleep(4)