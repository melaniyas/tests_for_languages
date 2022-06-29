import time
from selenium.webdriver.common.by import By


def test_busket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add_to_basket, 'кнопка добавления товара отсутвует'