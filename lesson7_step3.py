from selenium import webdriver
import time
import math

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector('input#answer').send_keys(y)
    #browser.find_element_by_css_selector('input.form-check-input').click()
    #browser.find_element_by_css_selector('#robotsRule').click()
    #browser.find_element_by_class_name('btn.btn-default').click()

    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"
    robots_radio = browser.find_element_by_id('robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    assert robots_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

