from selenium import webdriver
import time
import os

try:
    link="http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'try_load_file.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    #element = browser.find_element_by_css_selector('input[name="firstname"]')
    browser.find_element_by_css_selector("input[name='firstname']").send_keys('fvav')
    browser.find_element_by_css_selector("input[name='lastname']").send_keys('fvaddfffav')
    browser.find_element_by_css_selector("input[name='email']").send_keys('fvav@daf.com')
    element = browser.find_element_by_css_selector("input[id='file']")
    element.send_keys(file_path)
    browser.find_element_by_css_selector('.btn.btn-primary').click()

finally:
    time.sleep(15)
    browser.quit()

