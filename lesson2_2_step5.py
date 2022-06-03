# -*- coding: utf-8 -*-
from selenium import webdriver


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# noinspection PyDeprecation
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
# не забываем оставить пустую строку в конце файла

browser.exit()