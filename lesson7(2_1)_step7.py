# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #input_value
    
    x = browser.find_element_by_id('treasure').get_attribute("valuex")
    
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)
    
    input2 = browser.find_element_by_css_selector('#robotCheckbox')
    input2.click()
    
    input3 = browser.find_element_by_css_selector('#robotsRule')
    input3.click()
    
    
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()
    time.sleep(5)
    

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

