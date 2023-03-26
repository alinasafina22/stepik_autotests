"""
Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию, самостоятельно убедитесь в том что:
Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿
Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
Используемые селекторы должны быть уникальны
"""
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestLesson(unittest.TestCase):
    browser = webdriver.Chrome()
    link1 = 'http://suninjuly.github.io/registration1.html'
    link2 = 'http://suninjuly.github.io/registration2.html'

    def get_link_and_check(self, link):
        self.browser.get(link)
        # локаторы
        first_name_input = self.browser.find_element(By.CSS_SELECTOR, 'input.form-control.first')
        second_name_input = self.browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
        email_input = self.browser.find_element(By.CSS_SELECTOR, 'input.form-control.third')
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn')
        # Заполнение обязательных полей
        first_name_input.send_keys('Alina')
        second_name_input.send_keys('Zharkevich')
        email_input.send_keys('alinasafina22@gmail.com')
        submit_button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        sleep(5)
        final_text_elm = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        final_text = final_text_elm.text
        return final_text

    def test_first(self):
        assert "Congratulations! You have successfully registered!" == self.get_link_and_check(self.link1)

    def test_second(self):
        assert "Congratulations! You have successfully registered!" == self.get_link_and_check(self.link2)


if __name__ == "__main__":
    unittest.main()
