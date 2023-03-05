"""
Уникальность селекторов: часть 2
Попробуем реализовать один из автотестов из предыдущего шага. Вам дана страница с формой регистрации.
 Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *:
 First name, last name, email. Текст для полей может быть любым. Успешность регистрации проверяется
 сравнением ожидаемого текста "Congratulations! You have successfully registered!" с текстом на странице,
 которая открывается после регистрации. Для сравнения воспользуемся стандартной конструкцией assert из языка Python.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    first_name_input = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first')
    first_name_input.send_keys('Alina')
    second_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
    second_name_input.send_keys('Zharkevich')
    email_input = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third')
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
