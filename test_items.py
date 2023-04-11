from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_сheck_adding_to_сart(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket111")
        btn_check = True
    except:
        btn_check = False
    assert btn_check, "No add_card button on page"