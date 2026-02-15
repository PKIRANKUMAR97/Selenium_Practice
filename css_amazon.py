import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=5505922274072341199&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9184631&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")

search_item=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#twotabsearchtextbox")))
search_item.send_keys("Iphone 16 256 gb")
btn=driver.find_element(By.CSS_SELECTOR, "input.nav-input")
btn.click()
