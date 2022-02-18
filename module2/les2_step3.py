from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_css_selector("span#num1").text)
    num2 = int(browser.find_element_by_css_selector("span#num2").text)
    num_sum = num1 + num2
    select = Select(browser.find_element_by_css_selector("select#dropdown"))
    select.select_by_value(str(num_sum))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

except Exception as ex:
    print(repr(ex))

finally:
    time.sleep(10)
    browser.quit()