from selenium import webdriver as UwU
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/2/2.html"

with UwU.Chrome() as browser:
  browser.get(url)
  link = browser.find_element(By.LINK_TEXT, "16243162441624")
  link.click()
  result = browser.find_element(By.ID, "result")
  print(result.text)