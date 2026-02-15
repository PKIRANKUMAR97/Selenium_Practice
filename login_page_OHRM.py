from selenium.webdriver.common.by import By


def login(driver,username,password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    try:
        t1 = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").is_displayed()

        if t1:
            return True

    except:
        return False