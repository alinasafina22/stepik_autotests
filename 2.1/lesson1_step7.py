"""
Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
"""


from selenium.webdriver.common.by import By
from selenium import webdriver
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # Получаем значение X
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')  # получаем значение
    final_result = calc(x)  # Считаем значение Х в методе calc
    # Вводим полученное значение
    answer_inp = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer_inp.send_keys(final_result)
    # Выбираем checkbox и radiobutton
    checkbox_inp = browser.find_element(By.ID, "robotCheckbox")
    checkbox_inp.click()
    radio_btn = browser.find_element(By.ID, 'robotsRule')
    radio_btn.click()
    # Кликаем Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit_btn.click()
finally:
    sleep(10)
    browser.close()


