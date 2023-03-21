import time
from selenium.webdriver.common.by import By


def test_btn_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "button not found"
