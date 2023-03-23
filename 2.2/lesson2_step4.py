"""
What is ln(abs(12*sin(x))), where x = 360?
Открыть страницу https://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc_function(x):
    return math.log(abs(12*math.sin(x)))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# локаторы
value_inp = browser.find_element(By.ID, 'input_value')
answer_inp = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
checkbox_btn = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
radiobutton_btn = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')

try:
    x = int(value_inp.text)
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_inp)
    answer_inp.send_keys(str(calc_function(x)))
    checkbox_btn.click()
    radiobutton_btn.click()
    submit_btn.click()
finally:
    sleep(10)
    browser.close()





