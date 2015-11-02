from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
site_url = 'https://output.jsbin.com/radara'
driver.get(site_url)

try:
    email = driver.find_element_by_css_selector('#email')
    if email is not None:
        print 'TEST SUCCESS: email found'
except Exception as e:
    print 'TEST FAIL: email not found'

try:
    password = driver.find_element_by_css_selector('#password')
    if password is not None:
        print 'TEST SUCCESS: password found'
except Exception as e:
    print 'TEST FAIL: password not found'

try:
    submit_button = driver.find_element_by_css_selector('#login')
    if submit_button is not None:
        print 'TEST SUCCESS: submit button found'
except Exception as e:
    print 'TEST FAIL: submit button not found'

driver.quit()
