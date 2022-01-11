# -*- coding: utf-8 -*-
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name('form-control.first')
    input1.send_keys("Smolensk")
    input2 = browser.find_element_by_class_name('form-control.second')
    input2.send_keys("Smolensk")
    input3 = browser.find_element_by_class_name('form-control.third')
    input3.send_keys("Smolensk")
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

