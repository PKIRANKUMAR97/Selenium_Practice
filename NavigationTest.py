# Open site
# Click link
# Verify URL changed
# Verify title changed
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
mywait=WebDriverWait(driver,10)
driver.get("https://testautomationpractice.blogspot.com/")
url1=driver.current_url
title1=driver.title

print(url1)
print(title1)

p2=mywait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='merrymoonmary']")) )
p2.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])

url2=driver.current_url
title2=driver.title
print(url2)
print(title2)

if url1!=url2:
    print("url changed")
else:
    print("url not changed")

if title1!=title2:
    print("title changed")
else:
    print("title not changed")


