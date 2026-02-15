from driver_setup import get_driver
from login_page_OHRM import login

def test_valid_login():
    driver = get_driver()
    result_of_login_test=login(driver,"Admin","admin123")
    assert result_of_login_test is True

    driver.quit()