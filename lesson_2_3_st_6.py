# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input0 = browser.find_element_by_tag_name('button')
    input0.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    print(x)
    y = calc(x)
    
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(y))
    
   
    button = browser.find_element_by_css_selector('body > form > div > div > button')
    button.click()
    
    

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

