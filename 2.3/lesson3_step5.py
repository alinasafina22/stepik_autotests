'''
Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc_function(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn')

try:
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    x_text = browser.find_element(By.ID, 'input_value').text
    answer_inp = browser.find_element(By.ID, 'answer')
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    x_value = str(calc_function(int(x_text)))
    answer_inp.send_keys(x_value)
    submit_btn.click()
finally:
    sleep(5)
    browser.quit()
