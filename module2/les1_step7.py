from selenium import webdriver
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_css_selector("img#treasure").get_attribute("valuex"))
    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(str(calc(x)))
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()
    robotradio = browser.find_element_by_id("robotsRule")
    robotradio.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as ex:
    print(repr(ex))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()