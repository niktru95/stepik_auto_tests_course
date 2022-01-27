from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
img = browser.find_element(By.ID, 'treasure')
x_element = img.get_attribute('valuex')
x = x_element
y = calc(x)
input_answer = browser.find_element(By.ID, 'answer')
input_answer.send_keys(y)
robot_Checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_Checkbox.click()
robots_Rule = browser.find_element(By.ID, 'robotsRule')
robots_Rule.click()
submit_btn = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
submit_btn.click()
   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()