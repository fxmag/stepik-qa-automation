from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link='http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    result = str(math.log(abs(12 * math.sin(int(x)))))

    field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    #browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(result)

    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    browser.find_element_by_css_selector('[id="robotsRule"]').click()

    # Нажать кнопку "Submit"
    browser.find_element_by_css_selector('.btn.btn-primary').click()

finally:
    time.sleep(14)
    browser.quit()


