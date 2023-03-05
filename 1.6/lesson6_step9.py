"""
Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию, самостоятельно убедитесь в том что:
Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿
Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
Используемые селекторы должны быть уникальны
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    first_name_input = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first')
    first_name_input.send_keys('Alina')
    second_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block.second_class input')
    second_name_input.send_keys('Zharkevich')
    email_input = browser.find_element(By.CSS_SELECTOR, )
    email_input.send_keys('alinasafina22@gmail.com')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)

    final_text_elm = browser.find_element(By.TAG_NAME, 'h1')
    assert "Congratulations! You have successfully registered!" == final_text_elm.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
