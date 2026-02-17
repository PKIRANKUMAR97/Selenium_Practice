# 1. E-commerce End-to-End Automation;
# Use: Snapdeal / Amazon demo / Flipkart clone;
# Tasks; Search product; Apply filters (price + brand);
# Open product in new window; Add to cart;
# Verify: product name; price; cart count; --not done
# Concepts used; window handles; dynamic locators; assertions; waits
# 👉 Extension: remove product from cart; verify cart empty message -- not done

# 3. Search + Filter Automation (E-commerce);
# Task: Open shopping site;
# Search product;
# Apply filters (price/brand);
# Add to cart;
# Verify cart

import os
import time

from selenium.common import NoSuchElementException
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
search_txt.send_keys("watches for men")
search_txt.send_keys(Keys.ENTER)
mywait=WebDriverWait(driver,10)
action=ActionChains(driver)

min_price_txt=driver.find_element(By.XPATH,"//input[@name='fromVal']")
min_price_txt.clear()
min_price_txt.send_keys("300")

max_price_txt=driver.find_element(By.XPATH,"//input[@name='toVal']")
max_price_txt.clear()
max_price_txt.send_keys("1700")

max_price_txt.send_keys(Keys.ENTER)

# time.sleep(3)

display_analog_checkbox=driver.find_element(By.CSS_SELECTOR,"label[for='Display_s-Analog']")
driver.execute_script("arguments[0].click();", display_analog_checkbox)


# time.sleep(2)
dialshape_rectangular_checkbox=driver.find_element(By.CSS_SELECTOR,"label[for='DialShape_s-Rectangular']")
driver.execute_script("arguments[0].click();", dialshape_rectangular_checkbox)
# time.sleep(2)

starpmaterial_leather_checbox=driver.find_element(By.CSS_SELECTOR,"label[for='StrapMaterial_s-Leather']")
driver.execute_script("arguments[0].click();", starpmaterial_leather_checbox)
# time.sleep(2)

customer_rating_4star_radiobutton=driver.find_element(By.XPATH,"//label[@for='avgRating-4.0']")
driver.execute_script("arguments[0].click();", customer_rating_4star_radiobutton)
# time.sleep(2)


strap_color_brown_checkbox=driver.find_element(By.CSS_SELECTOR,"label[for='StrapColor_s-Brown']")
driver.execute_script("arguments[0].click();", strap_color_brown_checkbox)

product1=driver.find_element(By.CSS_SELECTOR,'p[title="HAMT Brown Leather Analog Men\'s Watch"]')
driver.execute_script("arguments[0].click();", product1)

product2=driver.find_element(By.XPATH,'//p[contains(@title,"LOUIS DEVIN - Brown Leather Analog")]')
driver.execute_script("arguments[0].click();", product2)


product3=driver.find_element(By.XPATH,"//p[contains(@title,'Reboot - Brown Leather Analog ')]")
driver.execute_script("arguments[0].click();", product3)


# product4=driver.find_element(By.XPATH,'//p[contains(@title,"Walrus WWM")]')
# driver.execute_script("arguments[0].click();", product4)

parent_window=driver.window_handles[0]

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if handle != parent_window:
        try:
            driver.find_element(By.XPATH, "//span[normalize-space()='add to cart']").click()
            time.sleep(2)
        except :
            print("No add to cart avaialable in this window ")




driver.find_element(By.XPATH,"//div[normalize-space()='View Cart']").click()

x = driver.find_element(By.XPATH,"//div[@id='cartModal']//h3[1]").text

assert x in "Shopping Cart "

print("we are in shopping cart page ")


print("Attempting to clear the shopping cart...")


while True:
    try:
        # Re-find the buttons every time to avoid StaleElement issues
        delete_buttons = driver.find_elements(By.CLASS_NAME, "remove-item-shortlist")
        if not delete_buttons:  ## if there are no items
            break

        driver.execute_script("arguments[0].click();", delete_buttons[0])
        print("Removed an item...")
        time.sleep(2)
    except:
        break

try:

    success = mywait.until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div[@id='cartModal']//h3"),
        "Shopping Cart is empty!"
    ))

    if success:
        final_text = driver.find_element(By.XPATH, "//div[@id='cartModal']//h3").text
        print(f"Success! Final Message: {final_text}")
        assert "empty" in final_text.lower()
        print("Done dude! Total Success.")
except Exception as e:
    print(f"Failed dude. Current header text is: {driver.find_element(By.XPATH, '//div[@id=\'cartModal\']//h3').text}")

