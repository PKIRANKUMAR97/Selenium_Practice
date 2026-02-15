from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.primevideo.com/region/eu/offers/nonprimehomepage/ref=dv_web_force_root")
print(driver.title)  ## Welcome to Prime Video
print(driver.current_url) ##https://www.primevideo.com/region/eu/offers/nonprimehomepage/ref=dv_web_force_root

print(driver.page_source)