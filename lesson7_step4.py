from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    treasure = browser.find_element_by_id('treasure')
    print(treasure)
    #Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x=treasure.get_attribute('valuex')
    #Посчитать математическую функцию от x (сама функция остаётся неизменной)
    result=str(math.log(abs(12 * math.sin(int(x)))))
    #Ввести ответ в текстовое поле
    browser.find_element_by_css_selector('input#answer').send_keys(result)
    #Отметить checkbox "I'm the robot"
    browser.find_element_by_css_selector('input#robotCheckbox').click()
    #Выбрать radiobutton "Robots rule!"
    browser.find_element_by_css_selector('input#robotsRule').click()
    #Нажать на кнопку "Submit"
    browser.find_element_by_css_selector('button.btn.btn-default').click()


finally:
    time.sleep(15)
    browser.quit()


