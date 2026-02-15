import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://cgi.njoyn.com/corp/xweb/xweb.asp?NTKN=c&page=joblisting&clid=21001")

wait = WebDriverWait(driver, 20)

##cookies check
try:
    cookies_accept_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Close')]")))
    cookies_accept_btn.click()

except:
    print("No cookie popup found")

btn=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Create your profile | Sign in"))).click()
driver.execute_script("arguments[0].scrollIntoView(true);", btn)
btn.click()
time.sleep(3)