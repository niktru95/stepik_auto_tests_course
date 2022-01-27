from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

magic_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
input_answer = browser.find_element(By.CLASS_NAME, 'form-control').send_keys(y)
btn_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(15)
browser.quit()
