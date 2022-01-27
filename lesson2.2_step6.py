from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
input_answer = browser.find_element(By.ID, 'answer').send_keys(y)
click_checkbox = browser.find_element(By.CLASS_NAME, 'form-check-label').click()
click_radiobtn = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", click_radiobtn)
click_radiobtn.click()
click_btn = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
browser.execute_script("return arguments[0].scrollIntoView(true);", click_btn)
click_btn.click()
   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()

