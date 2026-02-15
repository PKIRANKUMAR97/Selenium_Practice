# 🧪 Mini Project 4 — Broken Links Checker
# Concepts: find_elements, loop
# Site: any site
# Task
# Get all <a> tags
# Print links
# Print only links with "http"
# Count them

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
all_links = driver.find_elements(By.TAG_NAME,"a")

href_links=[]
for link in all_links:
    href=link.get_attribute("href")
    if href and "http" in href:
        print(href)
        href_links.append(href)
print(len(all_links))
print(len(href_links))