from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/1/1.html"

with webdriver.Chrome() as browser:
  browser.get(url)
  input_boxes = browser.find_elements(By.XPATH, "//div[@class='form_box']/input")
  for input_box in input_boxes:
    input_box.send_keys("Текст")
  button = browser.find_element(By.CLASS_NAME, "btn")
  button.click()
  result = browser.find_element(By.ID, "result")
  print(result.text)