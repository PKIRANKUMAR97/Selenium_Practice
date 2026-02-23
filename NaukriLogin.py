import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.naukri.com/")
driver.maximize_window()
mywait = WebDriverWait(driver, 10)

login_btn = driver.find_element(By.XPATH,"//a[@title='Jobseeker Login']")
login_btn.click()

driver.switch_to.frame(0)
time.sleep(12)
email_txt=mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']")))

email_txt.clear()
email_txt.send_keys("kumar@gmail.com")

password_txt=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
password_txt.clear()
password_txt.send_keys("99999999999999999999@PKK")

login_button=driver.find_element(By.XPATH," //button[@type='submit']")
login_button.click()

time.sleep(3)
my_name=driver.find_element(By.XPATH,"//div[contains(@title,'POLUPARTHI']")
if my_name.is_displayed():
    print("Passed")

else:
    print("Failed")
