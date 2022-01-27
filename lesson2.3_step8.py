import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
btn_book = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value').text
y = calc(x_element)
input_answer = browser.find_element(By.CLASS_NAME, 'form-control').send_keys(y)
btn_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(10)
browser.quit()