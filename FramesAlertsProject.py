# 🔹 3. Frames + Alerts Project;
# Site: https://the-internet.herokuapp.com/;
# Tasks; Handle iframe → type text JS alert → accept;
# confirmation alert → dismiss;
# prompt alert → send text;
# Concepts; switch_to.frame; switch_to.alert;
# validations
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# driver.get("https://the-internet.herokuapp.com/")
#
# driver.find_element(By.XPATH,"//a[text()='JavaScript Alerts']").click()
#
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
#
# my_alert1=driver.switch_to.alert
# my_alert1.accept()
#
# driver.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']").click()
# my_alert2=driver.switch_to.alert
# my_alert2.dismiss()
#
# driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']").click()
# my_alert3=driver.switch_to.alert
# my_alert3.send_keys("dudeeeeee")
# my_alert3.accept()



driver.get("https://vinothqaacademy.com/iframe/")

driver.switch_to.frame("employeetable")
print(driver.title)
time.sleep(10)


