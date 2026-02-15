from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
def login_2(username,password):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        mywait=WebDriverWait(driver,10)
        username_input=mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Username']")))
        password_input=mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()




        try:
            t1 = mywait.until(EC.presence_of_element_located((By.XPATH,"//h6[normalize-space()='Dashboard']")))
            x=t1.is_displayed()
            if x:
                print("Login Successful")
                return True

        except:
            print("Login Failed")
            return False

login_2("Admin","admin123")