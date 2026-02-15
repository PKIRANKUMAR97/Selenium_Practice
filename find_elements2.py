from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service= Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

l2=driver.find_elements(By.XPATH,"//div[@class='container']//a")
print(len(l2))