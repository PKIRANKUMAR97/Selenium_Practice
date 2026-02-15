from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service= Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/login")

l1=driver.find_elements(By.XPATH,"//a[@class='footer-menu__link']")
print(len(l1))