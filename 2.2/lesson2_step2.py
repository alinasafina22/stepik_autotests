from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects2.html'
browser.get(link)
# селекторы
num1_txt = int(browser.find_element(By.ID, 'num1').text)
num2_txt = int(browser.find_element(By.ID, 'num2').text)
dropdown_inp = Select(browser.find_element(By.CSS_SELECTOR, 'select#dropdown.custom-select'))
submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')

try:
    result = num1_txt + num2_txt
    dropdown_inp.select_by_value(str(result))
    submit_btn.click()
finally:
    sleep(20)
    browser.close()
