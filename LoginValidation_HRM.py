# Site:https://opensource-demo.orangehrmlive.com/
# Task:
# Open login page
# Enter username/password
# Click login
# Check Dashboard visible
# Print "Login success" or "Fail"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")
mywait=WebDriverWait(driver,10)
login=mywait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Username']")))

login.send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

dashboard = mywait.until(EC.presence_of_element_located((By.XPATH,"//h6[normalize-space()='Dashboard']")))
a= dashboard.is_displayed()
if a:
    print("login successful")
else:
    print("login failed")

driver.quit()



