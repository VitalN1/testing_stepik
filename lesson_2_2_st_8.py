# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import os
from selenium.webdriver.common.by import By



link1 = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("112@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file1.txt"
    file_path = os.path.join(current_dir, file_name)
    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)
    print(current_dir)
    print(file_path)
    
    
    
    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

