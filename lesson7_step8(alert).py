from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from sendToStepik import sendToStepik
import time

try:
    # в переменную task_link вставить адрес страницы с заданием
    #task_link = 'https://stepik.org/lesson/165493/step/5?unit=140087'

    link="http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('button.btn.btn-primary').click()

    #переключиться на окно с alert, а затем принять его с помощью команды accept():
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector('[id="input_value"]').text
    browser.find_element_by_css_selector('#answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_css_selector('button[type="submit"]').click()
    #Чтобы получить текст из alert, используйте свойство text объекта alert:
    # #alert = browser.switch_to.alert
    # #alert_text = alert.text
    # #согласиться с сообщением или отказаться
    # #confirm = browser.switch_to.alert
    # #confirm.accept()
    # #confirm.dismiss()

    # #prompt — имеет дополнительное поле для ввода текста
    # #prompt = browser.switch_to.alert
    # #prompt.send_keys("My answer")
    # #prompt.accept()
    # #pyperclip.copy(addToClipBoard) #добавить в буфер с помощью библиотеки pyperclip или можно с xclip, xsel

    # #для логина и пароля в модальном окне для переключения между логин и пароль используют
    # #prompt.send_keys(KEY.TAB)
    # Копирование числа из алерта

    # #alert = browser.switch_to.alert
    # #alert_text = alert.text
    # #alert.accept()
    # #answer = alert_text.split(': ')[-1]
    # #print(answer)
    # #time.sleep(1)

    # Отправка решения на степик
    # #sendToStepik(task_link, answer)
finally:
    time.sleep(15)
    browser.quit()



