from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.implicitly_wait(5)
signinbtn=driver.find_element(By.XPATH,"//input[@title='Search for Products, Brands and More']")
print(signinbtn.is_displayed())
print(signinbtn.is_enabled())
