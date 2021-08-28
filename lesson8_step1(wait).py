from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # browser.implicitly_wait(5)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 5).until(
    #    EC.element_to_be_clickable((By.ID, "verify"))
    # )
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    browser.find_element_by_css_selector('#book').click()
    time.sleep(1)

    field = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    x = browser.find_element_by_css_selector('span#input_value').text

    browser.find_element_by_css_selector('input#answer').send_keys((str(math.log(abs(12 * math.sin(int(x)))))))
    # button = browser.find_element_by_css_selector("button:not([disabled])") как пример
    # message = browser.find_element_by_id("verify_message")

    # assert "successful" in message.text
    browser.find_element_by_css_selector('button#solve.btn.btn-primary').click()

finally:
    time.sleep(15)
    browser.quit()


