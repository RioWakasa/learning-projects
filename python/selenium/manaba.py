from selenium import webdriver
from time import sleep

browser=webdriver.Chrome('desktop/chromedriver')
url='https://tsurumi-u.manaba.jp/ct/login'
browser.get(url)