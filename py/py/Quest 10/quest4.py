from selenium import webdriver as UwU
from selenium.webdriver.common.by import By
import time
url = "https://parsinger.ru/selenium/7/7.html"

with UwU.Chrome() as browser:
  browser.get(url)
  select = browser.find_element(By.ID, "opt")
  options = select.find_elements(By.XPATH, "option")
  option_total = 0
  for option in options:
    option_total += int(option.text)
  input_text = browser.find_element(By.ID, "input_result")
  input_text.send_keys(option_total)
  button = browser.find_element(By.ID, "sendbutton")
  button.click()
  result = browser.find_element(By.ID, "result")
  print(result.text)