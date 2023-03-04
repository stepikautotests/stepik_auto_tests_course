import unittest
from selenium import webdriver
import time

class Test_unittest(unittest.TestCase):
    def test_(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        element = browser.find_element_by_css_selector('div&gt;:nth-child(1)&gt;input')
        element.send_keys("Ivan")
        element = browser.find_element_by_css_selector('div&gt;:nth-child(2)&gt;input')
        element.send_keys("Ivan")
        element = browser.find_element_by_css_selector('div&gt;:nth-child(3)&gt;input')
        element.send_keys("Ivan")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue('Congratulations! You have successfully registered!',welcome_text)

if __name__ == '__main__':
    unittest.main()    