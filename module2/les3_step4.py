from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element_by_css_selector("button[type='submit']")
button.click()
alert = browser.switch_to.alert
alert.accept()
time.sleep(1)
x = int(browser.find_element_by_css_selector("span#input_value.nowrap").text)
input = browser.find_element_by_css_selector("[type='text']")
input.send_keys(str(calc(x)))
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()
