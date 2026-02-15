import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://careers.wipro.com/")

wait = WebDriverWait(driver, 20)

# accept cookies
try :
    accept_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept')]"))
    )
    accept_btn.click()
except:
    print("No cookie popup found")

# click Login

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

time.sleep(10)

# driver.implicitly_wait(15)
