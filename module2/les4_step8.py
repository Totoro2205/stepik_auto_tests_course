from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
    )
    button = browser.find_element_by_css_selector("button#book")
    # button = WebDriverWait(browser, 2).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button#book"))
    # )
    button.click()
    x = int(browser.find_element_by_css_selector("span#input_value.nowrap").text)
    input = browser.find_element_by_css_selector("[type='text']")
    input.send_keys(str(calc(x)))
    button = browser.find_element_by_css_selector("button#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except Exception as ex:
    print(repr(ex))

finally:
    time.sleep(5)
    browser.quit()
