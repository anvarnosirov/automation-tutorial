from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
site_url = 'https://output.jsbin.com/radara'
driver.get(site_url)
sleep(10)
driver.quit()
