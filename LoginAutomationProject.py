# Website idea: Any demo login site;
# Tasks: Launch browser;
# Enter username/password;
# Click login;
# Validate successful login;
# Capture screenshot on failure
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

def login_2(username, password):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # time.sleep(15)
        mywait = WebDriverWait(driver, 20)
        username_input = mywait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password_input = mywait.until(EC.element_to_be_clickable((By.NAME, "password")))
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()


        dashboard_presence = mywait.until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']"))).is_displayed()
        if dashboard_presence:
            print("Login Successful")

    except Exception as e:
        print(f"Login Failed: {e}")
        driver.save_screenshot(os.getcwd() + "//LoginFailed.png")
        

login_2("Admin", "admin123")


