from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
from math import log, sin

browser = webdriver.Chrome()
# browser=WebDriver()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    browser.find_element_by_css_selector(selector).click()

#    elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))

#    for elem in elements_to_select:
#        browser.find_element_by_css_selector(elem).click()