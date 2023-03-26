'''
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc_function(x):
    return math.log(abs(12 * math.sin(x)))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

try:
    book_btn = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_btn.click()
    x_text = browser.find_element(By.ID, 'input_value').text
    answer_inp = browser.find_element(By.ID, 'answer')
    submit_btn = browser.find_element(By.ID, 'solve')
    x_value = str(calc_function(int(x_text)))
    answer_inp.send_keys(x_value)
    submit_btn.click()
finally:
    browser.quit()