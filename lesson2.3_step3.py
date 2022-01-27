import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
first_name = browser.find_element(By.NAME, 'firstname').send_keys('test')
second = browser.find_element(By.NAME, 'lastname').send_keys('test')
email = browser.find_element(By.NAME, 'email').send_keys('test@test.com')
current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'text.txt')
element = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)           
submit_btn = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(15)
browser.quit()
