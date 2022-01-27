from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
input_answer = browser.find_element(By.ID, 'answer').send_keys(y)
# input_answer.send_keys(y)
click_checkbox = browser.find_element(By.CLASS_NAME, 'form-check-label').click()
# click_checkbox.click()
click_radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
# click_radiobtn.click()
click_btn = browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
# click_btn.click()
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()