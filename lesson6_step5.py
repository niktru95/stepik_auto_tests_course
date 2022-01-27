from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    first_name = browser.find_element_by_tag_name('input')
    first_name.send_keys('Коля')
    last_name = browser.find_element_by_name('last_name')
    last_name.send_keys('Трушников')
    city = browser.find_element_by_class_name('form-control.city')
    city.send_keys('Мурманск')
    country = browser.find_element_by_id('country')
    country.send_keys('Россия')
    btn = browser.find_element_by_class_name('btn.btn-default')
    btn.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла