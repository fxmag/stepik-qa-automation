import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects1.html'

with webdriver.Chrome() as b:
    #     Открываем страницу в браузере
    b.get(url)

    #     Находим все цыфры в строке и добавляем их в список
    numb_list = [int(i.text) for i in
                 b.find_elements_by_css_selector('h2 .nowrap')
                 if i.text.isdecimal()]

    #     открываем выпадающий список
    #     b.find_element_by_id('dropdown').click()
    select = Select(b.find_element_by_tag_name('select'))

    #     ищем ответ в списке и выбираем его
    #     b.find_element_by_css_selector(f'[value = "{sum(numb_list)}"]').click()
    select.select_by_value(f'{sum(numb_list)}')

    #     находим кнопку и жмакаем
    b.find_element_by_class_name('btn').click()

    #     ловим алерт и забираем из него ответ
    print(b.switch_to.alert.text.split()[-1])