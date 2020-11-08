import pytest
from selenium import webdriver
import time


# @pytest.mark.parametrize('language', ["es", "en-gb"])
def test_guest_should_see_login_link(browser,language):
    lang = language  #присваиваем переменной lang
    link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    selector = "#add_to_basket_form button"
    time.sleep(1)
    def is_element_present(browser):
        try:
            browser.implicitly_wait(30)
            browser.find_element_by_css_selector(selector)
            return True
        except:
            return False
    # z = is_element_present(browser)
    # print("zzzzzz= ",z)
    # assert z == True, "корзинка не найдена"
    assert is_element_present(browser) == True, "корзинка не найдена"
    browser.find_element_by_css_selector(selector).click()
    time.sleep(1)
