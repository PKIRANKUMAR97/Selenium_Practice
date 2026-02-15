from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.facebook.com/r.php")

day_element=driver.find_element(By.ID, "day")
day=Select(day_element)
day.select_by_visible_text("6")

print("Selected Day", day.first_selected_option.text)

month_element=driver.find_element(By.ID, "month")
month=Select(month_element)
month.select_by_value("6")

print("Selected Month", month.first_selected_option.text)

year_element=driver.find_element(By.ID, "year")
year=Select(year_element)
year.select_by_index(5)

print("Selected Year", year.first_selected_option.text)
