# 🧪 Mini Project 3 — Amazon Search Count
# Concepts: CSS selector, list elements
# Task
# Search "iphone"
# Count number of product titles
# Print count
# Print first product name
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.maximize_window()
mywait = WebDriverWait(driver, 20)
driver.get("https://www.amazon.in/")
search_bar = mywait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
search_bar.send_keys("iphone")
search_bar.send_keys(Keys.ENTER)

product_titles=mywait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"span.a-size-medium")))
print(len(product_titles))
print(product_titles[0].text)

