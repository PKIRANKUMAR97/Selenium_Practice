# 2. Web Table Automation (OrangeHRM);
# Site: https://opensource-demo.orangehrmlive.com;
# Tasks; Login; Go to Admin → Users table;
# Print all playernames;
# Count rows;
# Find a specific playername;
# Delete user;
# Verify deletion;
# Concepts; dynamic XPath; loops; tables; explicit waits

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from Selenium_Practice.LoginAutomationProject import login_2

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# login_2("Admin","admin123")

driver.get("https://www.bcci.tv/international/men/stats/test")

total_rows= driver.find_elements(By.XPATH,"//table/tbody/tr")
print(len(total_rows))
