# -*- coding: utf-8 -*-
from selenium import webdriver
import time
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# noinspection PyDeprecation
browser.find_element(by=By.TAG_NAME, value=name)

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
# не забываем оставить пустую строку в конце файла
time.sleep(10)
browser.close()
