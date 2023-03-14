"""
What is ln(abs(12*sin(x))), where x = 311?
Ваша программа должна выполнить следующие шаги:

Открыть страницу https://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
"""


from selenium.webdriver.common.by import By
from selenium import webdriver
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # Получаем значение X
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    final_result = calc(x)  # Считаем значение Х в методе calc
    # Вводим полученное значение
    answer_inp = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    answer_inp.send_keys(final_result)
    # Выбираем checkbox и radiobutton
    checkbox_inp = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox_inp.click()
    radio_btn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_btn.click()
    # Кликаем Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit_btn.click()
finally:
    sleep(10)
    browser.close()


