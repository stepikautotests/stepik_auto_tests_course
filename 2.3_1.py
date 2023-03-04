from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
browser = webdriver.Chrome()
link='http://suninjuly.github.io/redirect_accept.html'
browser.get(link)
#alert = browser.switch_to.alert
#alert.accept()



button = browser.find_element(By.TAG_NAME, 'button')
button.click()

old_window = browser.window_handles[0]
browser.switch_to.window(old_window)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)




#confirm = browser.switch_to.alert
#confirm.accept()
a=browser.find_element(By.ID, "input_value").text
a=int(a)

def funk(a):
    
    return math.log(abs(12*math.sin(a)))

browser.find_element(By.ID, "answer").send_keys(str(funk(a)))

browser.find_element(By.TAG_NAME, "button").click()
