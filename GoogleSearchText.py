import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.google.com")

searchbox= driver.find_element(By.XPATH,"//textarea[@jsname='yZiJbe' and @class='gLFyf']")
searchbox.send_keys("Python Selenium")
searchbox.send_keys(Keys.ENTER)
time.sleep(7)
print(driver.title)

if "Python" in driver.title:
    print("Yes")
else:
    print("No")