import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login_test():
    # driver = webdriver.Chrome(service=ChromeDriverManager().install())

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

    t1 = driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()

    if t1:
        return True

    else :
        return False

if login_test():
    print("Login Successful")
else :
    print("Login Failed")



