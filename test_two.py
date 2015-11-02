from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
site_url = 'https://output.jsbin.com/radara'
driver.get(site_url)

try:
    email = driver.find_element_by_css_selector('#email')
    if email!=None:
        print 'TEST SUCCESS: email found'
except Exception as e:
    print 'TEST FAIL: email not found'

driver.quit()
