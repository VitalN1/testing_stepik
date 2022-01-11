# -*- coding: utf-8 -*-
from selenium import webdriver
import time 


link = "http://suninjuly.github.io/selects2.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #input_value
    
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    res = str(int(x) + int(y))
    browser.find_element_by_tag_name("select").click()
    
    # browser.find_element_by_css_selector(f'[value={res}]').click()
    print(F'[value="{res}"]')
    browser.find_element_by_css_selector(F'[value="{res}"]').click()
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

