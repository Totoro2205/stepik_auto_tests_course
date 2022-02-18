''' 1 задание
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))
'''





'''import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://kzn.rpa-mu.ru/")
time.sleep(1)

textarea = driver.find_element_by_css_selector("/Users/Account/LogOn?ReturnUrl=%2F")
#textarea = driver.find_element_by_css_selector(".textbox")
submit_button.click()
'''







'''
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
# закрываем браузер после всех манипуляций
    browser.quit()
'''








'''
#https://stepik.org/lesson/138920/step/4?unit=196194
from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_id("submit_button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (для линукса)
'''








'''
#https://stepik.org/lesson/138920/step/5?unit=196194
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

#str(math.ceil(math.pow(math.pi, math.e)*10000))

link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(30)
'''











'''
#https://stepik.org/lesson/138920/step/7?unit=196194
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("_")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''








'''
# https://stepik.org/lesson/138920/step/8?unit=196194
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    element = browser.find_element_by_xpath("//button[@type = 'submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''













# 2.1 Основные методы Selenium
# Уникальность селекторов: часть 2
# https://stepik.org/lesson/138920/step/10?unit=196194

from selenium import webdriver
from time import sleep

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[@placeholder = 'Input your first name']") # First name*
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']") # Last name*
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder = 'Input your email']") # Email*
    input3.send_keys("1@ya.ru")
    sleep(3)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(2)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
    











'''
# 2.1 Основные методы Selenium
# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
# https://stepik.org/lesson/165493/step/5
# Ваша программа должна выполнить следующие шаги:
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

from selenium import webdriver
from time import sleep
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    robotCheckbox = browser.find_element_by_css_selector("[for = 'robotCheckbox']").click()
    robotsRule = browser.find_element_by_css_selector("[for='robotsRule']").click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
'''









'''
# 2.1 Основные методы Selenium
# https://stepik.org/lesson/165493/step/7?unit=140087
# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу,
# как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке",
# точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

from selenium import webdriver
from time import sleep
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #x = browser.find_element_by_xpath("//div/label/span[@id = 'input_value']").text
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    robotCheckbox = browser.find_element_by_id('robotCheckbox').click()
    robotsRule = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
'''













'''
# Работа с файлами, списками и js-скриптами
# https://stepik.org/lesson/228249/step/6?unit=200781

# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться
# с ужасным и огромным футером, который дизайнер всё никак не успевает переделать.
# Вам потребуется написать код, чтобы:
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение
# по времени), вы увидите окно с числом. Отправьте полученное число в качестве
# ответа для этого задания. Для этой задачи вам понадобится использовать метод
# execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from math import log, sin

try:
    # Открыть страницу:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Считать значение для переменной x:
    x = browser.find_element_by_id('input_value').text

    # Посчитать математическую функцию от x:
    y = log(abs(12*sin(int(x))))

    # Ввести ответ в текстовое поле:
    input = browser.find_element_by_id('answer').send_keys(y)
    
    # Проскроллить страницу вниз:
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    robotCheckbox = browser.find_element_by_id('robotCheckbox').click()
    robotsRule = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
'''










'''

# 2.2 Работа с файлами, списками и js-скриптами
# https://stepik.org/lesson/228249/step/8?unit=200781

# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.
# Напишите скрипт, который будет выполнять следующий сценарий:
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
# Если все сделано правильно и быстро, вы увидите окно с числом.
# Отправьте полученное число в качестве ответа для этого задания.

from selenium import webdriver
from time import sleep
import os

# Создадим файл example.txt в текущей папке (там же где лежит этот код)
with open("example.txt", "w") as file:
    file.write("бла-бла-бла))")

try:
    # Открыть страницу:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[@placeholder = 'Enter first name']") # First name*
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder = 'Enter last name']") # Last name*
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder = 'Enter email']") # Email*
    input3.send_keys("1@ya.ru")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)      # просто проверка)

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'example.txt')
    print(file_path)        # просто проверка)

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

os.remove(file_path)            # удаляем созданный файл

'''











'''

# 2.3 Работа с окнами
# https://stepik.org/lesson/184253/step/4

# Задание: принимаем alert
# Hаписать программу, которая будет выполнять следующий сценарий:
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро вы увидите окно с числом.
# Отправьте полученное число в качестве ответа на это задание.

from selenium import webdriver
from time import sleep
from math import log, sin

try:
    # Открыть страницу:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()
    sleep(2)

    # Считать значение для переменной x:
    x = browser.find_element_by_id('input_value').text

    # Посчитать математическую функцию от x:
    y = log(abs(12*sin(int(x))))

    # Ввести ответ в текстовое поле:
    input = browser.find_element_by_id('answer').send_keys(y)

    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

'''











'''

# 2.3 Работа с окнами
# https://stepik.org/lesson/184253/step/6

# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
# Сценарий для реализации выглядит так:
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро, вы увидите окно с числом.
# Отправьте полученное число в качестве ответа на это задание.

from selenium import webdriver
from time import sleep
from math import log, sin

try:
    # Открыть страницу:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()

    browser.switch_to.window(browser.window_handles[1])

    # Считать значение для переменной x:
    x = browser.find_element_by_id('input_value').text

    # Посчитать математическую функцию от x:
    y = log(abs(12*sin(int(x))))

    # Ввести ответ в текстовое поле:
    input = browser.find_element_by_id('answer').send_keys(y)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''











'''
# 2.4 Настройка ожиданий
# https://stepik.org/lesson/181384/step/8

# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом
# для отдыха по строго заданной цене. Более высокая цена нас не устраивает,
# а по более низкой цене объект успеет забронировать кто-то другой.
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод
# text_to_be_present_in_element из библиотеки expected_conditions.
# Если все сделано правильно и быстро, то вы увидите окно с числом.
# Отправьте его в качестве ответа на это задание.

from selenium import webdriver
from time import sleep
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Открыть страницу:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим WebDriver ждать ВСЕ элементы в течение 12 секунд
    #browser.implicitly_wait(12)
    # Implicit wait (неявное ожидание) - его не надо явно указывать каждый раз, используется для ожидания прогрузки страницы.
    # Explicit Waits (явное ожидание) - позволяют задать специальное ожидание для конкретного элемента (см.ниже ждем когда цена станет равна $100.
    # Например, кнопка стала кликабельной или кнопка становится неактивной после отправки данных.
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element_by_css_selector("button.btn").click()

    # Считать значение для переменной x:
    x = browser.find_element_by_id('input_value').text

    # Посчитать математическую функцию от x:
    y = log(abs(12*sin(int(x))))

    # Ввести ответ в текстовое поле:
    input = browser.find_element_by_id('answer').send_keys(str(y))  #не забыв перевести число в строку, чтобы передать в keys

    button = browser.find_element_by_id("solve").click() 
    # здесь css_selector("button.btn") не работает, потому что у нас уже вторая кнопка с таким "тег.класс"
    # поэтому ищем по "id"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта и скопировать полученный результат в буфер обмена
    sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''













'''
# Самостоятельное задание - залогиниться, перейти на урок и нажать радиобаттон 

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

mail = 'ccccccc@mail.ru'
password = 'cccccccc'

try:
    # Открыть страницу:
    link = "https://stepik.org"
    #link_lesson = "https://stepik.org/lesson/236205/step/3?unit=208637"
    link_lesson = "https://stepik.org/lesson/236205/step/3"
    browser = webdriver.Firefox()    # .Chrome()
    browser.get(link)

    browser.find_element_by_link_text ("Войти").click()  #войти

    input1 = browser.find_element_by_id('id_login_email').send_keys(mail)
    input2 = browser.find_element_by_id('id_login_password').send_keys(password)  #нужен реальный пароль
    browser.find_element_by_css_selector("button.sign-form__btn").click()  #полный класс: sign-form__btn button_with-loader
    browser.get(link_lesson)

    browser.find_element_by_css_selector("browser.switch_to.alert").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта и скопировать полученный результат в буфер обмена
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
