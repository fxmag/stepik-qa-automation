from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link='http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать сумму заданных чисел
    x = int(browser.find_element_by_id('num1').text)+int(browser.find_element_by_id('num2').text)
    x_str = str(x)
    #Выбрать в выпадающем списке значение равное расчитанной сумме
    browser.find_element_by_tag_name("select").click()

    #browser.find_element_by_css_selector("[value='1']").click()
    browser.find_element_by_css_selector("[value='" + x_str + "']").click()
    #browser.find_element_by_css_selector(f"[value='{x_str}']")

    #select = Select(browser.find_element_by_css_selector("select"))
    #select.select_by_value(str(x))


    # Нажать кнопку "Submit"
    browser.find_element_by_css_selector('.btn.btn-default').click()

finally:
    time.sleep(14)
    browser.quit()


