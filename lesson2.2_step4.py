from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
sum_1 = browser.find_element(By.ID, 'num1')
sum_2 = browser.find_element(By.ID, 'num2')
new_sum_1 = int(sum_1.text)
new_sum_2 = int(sum_2.text)
sum_1_2 = str(new_sum_1 + new_sum_2)
select_1 = browser.find_element(By.ID, 'dropdown')
select_1.click()
select_2 = Select(browser.find_element(By.ID, 'dropdown'))
select_2.select_by_visible_text(sum_1_2)
submit_btn = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
submit_btn.click()
   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()

