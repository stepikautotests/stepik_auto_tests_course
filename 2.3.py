from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
browser = webdriver.Chrome()
link='http://suninjuly.github.io/alert_accept.html'
browser.get(link)
button = browser.find_element(By.TAG_NAME, 'button')
button.click()
confirm = browser.switch_to.alert
confirm.accept()
a=browser.find_element(By.ID, "input_value").text
a=int(a)

def funk(a):
    
    return math.log(abs(12*math.sin(a)))

browser.find_element(By.ID, "answer").send_keys(str(funk(a)))

browser.find_element(By.TAG_NAME, "button").click()