
from selenium import webdriver
import time
import pytest

def test_1():

    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_css_selector('body > div.container > form > div.first_block > div.form-group.first_class > input')
    element.send_keys("Ivan")
    element = browser.find_element_by_css_selector('body > div.container > form > div.first_block > div.form-group.second_class > input')
    element.send_keys("Ivan")
    element = browser.find_element_by_css_selector('body > div.container > form > div.first_block > div.form-group.third_class > input')
    element.send_keys("Ivan")
    
    element = browser.find_element_by_css_selector('body > div.container > form > div.second_block > div.form-group.first_class > input')
    element.send_keys("Ivan")
    
    element = browser.find_element_by_css_selector('body > div.container > form > div.second_block > div.form-group.second_class > input')
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

    assert 'Congratulations! You have successfully registered!' == welcome_text

def test_2():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_css_selector('body > div.container > form > div.first_block > div.form-group.first_class > input')
    element.send_keys("Ivan")
    element = browser.find_element_by_css_selector('body > div.container > form > div.first_block > div.form-group.second_class > input')
    element.send_keys("Ivan")
    element = browser.find_element_by_css_selector('body > div.container > form > div.first_block > div.form-group.third_class > input')
    element.send_keys("Ivan")
    
    element = browser.find_element_by_css_selector('body > div.container > form > div.second_block > div.form-group.first_class > input')
    element.send_keys("Ivan")
    
    element = browser.find_element_by_css_selector('body > div.container > form > div.second_block > div.form-group.second_class > input')
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

    assert 'Congratulations! You have successfully registered!' == welcome_text

  
if __name__ == '__main__':
    pytest.main()