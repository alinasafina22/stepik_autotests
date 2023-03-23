'''
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

# строки, которые будем вводить
name = 'Alina'
last_name = 'Zharkevich'
email_address = 'ar.zharkevich@gmail.com'
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


# локаторы
first_name_inp = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
last_name_inp = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
email_inp = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
file_btn = browser.find_element(By.ID, 'file')
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')

try:
    first_name_inp.send_keys(name)
    last_name_inp.send_keys(last_name)
    email_inp.send_keys(email_address)
    file_btn.send_keys(file_path)
    submit_btn.click()
finally:
    browser.close()