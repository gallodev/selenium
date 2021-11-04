from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://github.com/'

def init_driver(URL):
    firefox = webdriver.Firefox()
    firefox.get(URL)
    return firefox

def wait(driver):
    driver.implicitly_wait(500)

def close(driver):
    driver.close()

driver = init_driver(URL)

form = driver.find_element(By.CLASS_NAME,'js-site-search-form')
driver.find_element(By.NAME,'q').send_keys('Selenium')
form.submit()

wait(driver)

menu = driver.find_element(By.CLASS_NAME,"menu")
menuSelected = menu.find_element(By.CLASS_NAME,"selected")

assert "Repositories" in menuSelected.text
print("Repositorieis - "+ menuSelected.text)

close(driver)