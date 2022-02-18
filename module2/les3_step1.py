from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
browser.execute_script("alert('Hello!!!');")
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(2)
alert.accept()
browser.quit()
