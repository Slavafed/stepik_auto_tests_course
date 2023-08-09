from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

try: 
    link = "https://SunInJuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
  
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('FED')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('OR')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('yp@DEAD')
    # Отправляем заполненную форму
  
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
    lf = browser.find_element(By.NAME, "file")
    lf.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    button.click()

 
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()