import unittest
from selenium import webdriver

class MyTest_1(unittest.TestCase):
    def test_first(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        browser.find_element_by_class_name('form-control.first').send_keys('test')
        browser.find_element_by_class_name('form-control.second').send_keys('test')
        browser.find_element_by_class_name('form-control.third').send_keys('test')
        browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input').send_keys('test')
        browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input').send_keys('test')
        browser.find_element_by_class_name('btn.btn-default').click()
        text_congrats = browser.find_element_by_tag_name('h1').text
        self.assertEqual()
    def test_second(self):
       browser = webdriver.Chrome()
       browser.get("http://suninjuly.github.io/registration2.html")
       browser.find_element_by_class_name('form-control.first').send_keys('test')
       browser.find_element_by_class_name('form-control.second').send_keys('test')
       browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input').send_keys('test')
       browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input').send_keys('test')
       browser.find_element_by_class_name('btn.btn-default').click()

if __name__ == "__main__":
    unittest.main()

 

    