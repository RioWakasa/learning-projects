from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome('desktop/chromedriver')
url='https://www.google.co.jp'
driver.get(url)
search_bar = driver.find_element(By.CSS_SELECTOR, "name")('q')
#search_bar.send_key('python')