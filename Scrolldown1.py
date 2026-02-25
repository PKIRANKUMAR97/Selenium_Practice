import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
webdriver = webdriver.Chrome(service=service)
webdriver.maximize_window()
webdriver.get("https://www.python.org")


mywait = WebDriverWait(webdriver, 10)
logo=mywait.until(EC.presence_of_element_located((By.XPATH,"//li[@role='treeitem']//a[normalize-space()='Python Logo']")))
webdriver.execute_script("arguments[0].scrollIntoView(true);", logo)
logo.click()
webdriver.execute_script("window.scrollTo(0, 0);")

webdriver.quit()


