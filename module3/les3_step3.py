from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Для успешного прохождения теста нужно выполнить из терминала
pytest ./module3/les3_step3.py
и скопировать результат между знаками равенства
"""

def test_uniq_selector1():
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/registration1.html"
    browser.get(url)
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("usr@i.ua")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Registration error!!!'


def test_uniq_selector2():
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/registration2.html"
    browser.get(url)
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("usr@i.ua")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Registration error!!!'

