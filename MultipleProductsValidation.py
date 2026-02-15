# 🧪 Mini Project 6 — Multiple Products Validation
# Amazon again.
# Task
# Search "laptop"
# Store first 5 product names in list
# Print them
# Check if any contains "HP"
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
mywait = WebDriverWait(driver,10)

driver.get("https://www.amazon.in/")
search_bar = mywait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='twotabsearchtextbox']") ))

search_bar.send_keys("laptop")
search_bar.send_keys(Keys.ENTER)

products= mywait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[data-component-type='s-search-result'] h2 span")))

for p in products[0:5]:
    print(p.text)
driver.implicitly_wait(5)

