import pytest
from selenium import webdriver
import time


# @pytest.mark.parametrize('language', ["es", "en-gb"])
def test_guest_should_see_login_link(browser,language):
    print("language in tist_items = ", language)
    lang = language
    link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(2)
    browser.find_element_by_css_selector("#add_to_basket_form button").click()
    time.sleep(10)