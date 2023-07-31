from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import math
from time import sleep

browser = webdriver.Chrome()
LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def solve_quiz_and_get_code():
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


def add_to_card():
    browser.get(LINK)
    add_button = browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket')
    add_button.click()
    solve_quiz_and_get_code()

def final_check():
    sleep(10)
    is_true = browser.find_element(By.CSS_SELECTOR, '.alertinner')
    code = "The shellcoder's handbook был добавлен в вашу корзину."
    return is_true.text == code

