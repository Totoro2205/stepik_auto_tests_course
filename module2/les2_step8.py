from selenium import webdriver
import time
import os

try:
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sample.txt')
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input[name='firstname']")
    last_name = browser.find_element_by_css_selector("input[name='lastname']")
    email = browser.find_element_by_css_selector("input[name='email']")
    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("ua@i.ua")
    file_button = browser.find_element_by_css_selector("input#file")
    file_button.send_keys(file_path)
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

except Exception as ex:
    print(repr(ex))

finally:
    time.sleep(10)
    browser.quit()
