# Automate a registration form:
# Text fields;
# Radio buttons;
# Checkboxes;
# Dropdown;
# Submit form;
# Validate success message

import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("kiran")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("kumar")


driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("Hyderabd,India")
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("kiaran@gmail.comn")
driver.find_element(By.CSS_SELECTOR,"input[type='tel']").send_keys("9999999999")

male_radio = (driver.find_element(By.XPATH,"//input[@value='Male']"))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",male_radio)
male_radio.click()
driver.find_element(By.XPATH,"//input[@id='checkbox2']").click()
driver.find_element(By.XPATH,"//div[@id='msdd']").click()
hindi_chk=driver.find_element(By.XPATH,"//a[normalize-space()='Hindi']")
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",hindi_chk)
hindi_chk.click()

english_chk=driver.find_element(By.XPATH,"//a[normalize-space()='English']")
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",english_chk)
english_chk.click()
drp_dwn_skill=driver.find_element(By.XPATH,"//select[@id='Skills']")
skill = Select(drp_dwn_skill)
skill.select_by_value("Android")

select_country_drp_dwn=driver.find_element(By.XPATH,"//span[@role='combobox']")
select_country_drp_dwn.click()

select_txt=driver.find_element(By.XPATH,"//input[@role='textbox']")
select_txt.send_keys("India")
select_txt.send_keys(Keys.ENTER)



year_box=driver.find_element(By.XPATH,"//select[@id='yearbox']")
year=Select(year_box)
year.select_by_value("1975")

month_box=driver.find_element(By.XPATH,"//select[@placeholder='Month']")
month=Select(month_box)
month.select_by_value("January")

date_box=driver.find_element(By.XPATH,"//select[@id='daybox']")
date=Select(date_box)
date.select_by_value("6")

driver.find_element(By.XPATH,"//input[@id='firstpassword']").send_keys("1234567890")
driver.find_element(By.XPATH,"//input[@id='secondpassword']").send_keys("1234567890")

driver.find_element(By.XPATH,"//input[@id='imagesrc']").send_keys("E:\KIRAN\Documents\Kiran Photo.jpg")


# driver.find_element(By.XPATH,"//button[@id='submitbtn']").click()

time.sleep(5)



