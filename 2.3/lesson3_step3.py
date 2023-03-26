'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
 ln(abs(12*sin(x))), where x = 395
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc_function(x):
    return math.log(abs(12*math.sin(x)))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')


try:
    button.click()
    alert = browser.switch_to_alert()
    alert.accept()
    # локаторы на следующей странице
    x_text = browser.find_element(By.ID, 'input_value').text
    answer_inp = browser.find_element(By.ID, 'answer')
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    x_value = str(calc_function(int(x_text)))
    answer_inp.send_keys(x_value)
    submit_btn.click()
finally:
    sleep(10)
    browser.close()
