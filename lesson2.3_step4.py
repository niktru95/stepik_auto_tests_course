import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
confirm = browser.switch_to.alert.accept()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
input_answer = browser.find_element(By.CLASS_NAME, 'form-control').send_keys(y)
btn_second = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(15)
browser.quit()
