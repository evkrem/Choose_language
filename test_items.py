import time



def test_add_to_cart_button_is_displayed(browser,language):
    lang = language  #присваиваем переменной lang
    link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    selector = "#add_to_basket_form button"
    #time.sleep(30)
    def is_element_present(browser):
        try:
            browser.implicitly_wait(5)
            browser.find_element_by_css_selector(selector)
            return True
        except:
            return False
    assert is_element_present(browser) == True, "корзинка не найдена"
    browser.find_element_by_css_selector(selector).click()
    time.sleep(1)
