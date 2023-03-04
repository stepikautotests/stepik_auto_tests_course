from selenium import webdriver
from selenium.webdriver.common.by import By
import os
current_dir = os.path.abspath(os.path.dirname(r'C:\Users\PC\обучение\1'))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
browser.find_element(By.CSS_SELECTOR, "input:nth-child(2)").send_keys("Maxim")

browser.find_element(By.CSS_SELECTOR, "input:nth-child(4)").send_keys("Solovyev")

browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)").send_keys("solovev.maxim@list.ru")
browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
button = browser.find_element(By.TAG_NAME, 'button')
button.click()