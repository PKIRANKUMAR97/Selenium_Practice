import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@title='Search for Products, Brands and More']").send_keys("Iphone 16 256 gb")
driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']").click()

driver.find_element(By.XPATH,"//*[text()='Apple iPhone 16 (Black, 256 GB)']").click()
time.sleep(5)