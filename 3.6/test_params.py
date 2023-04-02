'''
Переделать по нормальному
вынести авторизацию
уменьшить параметризацию
Сделать page object версию
'''
import time
import math
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1)'])
def test_params(link, browser):
    try:
        browser.get(link)
        browser.implicitly_wait(30)
        login_btn = browser.find_element(By.CSS_SELECTOR, 'a#ember33')
        # TODO установить умные ожидания
        time.sleep(10)
        login_btn.click()
        time.sleep(5)
        email_inp = browser.find_element(By.ID, 'id_login_email')
        password_inp = browser.find_element(By.ID, 'id_login_password')
        submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader')
        email_inp.send_keys('login')
        password_inp.send_keys('password')
        submit_btn.click()
        time.sleep(10)
        answer_int = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
        response = str(math.log(int(time.time())))
        answer_int.send_keys(response)
        submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        submit_btn.click()
        hint_txt = browser.find_element(By.CSS_SELECTOR, '.smart-hints')
        result_fin = hint_txt.text
        assert result_fin == 'Correct!', result_fin
    except NoSuchElementException:
        answer_int = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
        response = str(math.log(int(time.time())))
        answer_int.send_keys(response)
        submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        submit_btn.click()
        hint_txt = browser.find_element(By.CSS_SELECTOR, '.smart-hints')
        result_fin = hint_txt.text
        assert result_fin == 'Correct!', result_fin
    browser.quit()
