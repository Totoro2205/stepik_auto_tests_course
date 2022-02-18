from selenium import webdriver
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num = browser.find_element_by_id("input_value").text
    print(num)

    y = calc(num)
    input = browser.find_element_by_id('answer').send_keys(y)
    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]').click()
    radiobtn = browser.find_element_by_id('robotsRule').click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()