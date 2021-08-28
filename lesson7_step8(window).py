from selenium import webdriver
import math
import time
try:
    link="http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_window = browser.current_window_handle

    browser.find_element_by_class_name('trollface.btn.btn-primary').click()
    new_window = browser.window_handles[2]
    browser.switch_to.window(new_window)
    x=browser.find_element_by_css_selector('span[id="input_value"]').text
    browser.find_element_by_css_selector('#answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_css_selector('button.btn.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()

