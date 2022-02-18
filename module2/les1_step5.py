from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_css_selector("span#input_value.nowrap").text)
    input = browser.find_element_by_css_selector("[type='text']")
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
    time.sleep(10)
    browser.quit()
