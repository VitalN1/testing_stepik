# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    alert_btn = browser.find_element_by_tag_name('button')
    alert_btn.click()
    browser.switch_to.alert.accept()
    
    x = browser.find_element_by_id('input_value').text
    print(x)
    y = calc(x)
    
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(y))
    
   
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    time.sleep(1)
    

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

