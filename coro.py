from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("/path/to/chromedriver")
driver.get('https://app.humancloud.co.in')
driver.maximize_window()

menu_btn=driver.find_element('id','landPartner')
menu_btn.click()
time.sleep(1)
username=driver.find_element('id','logInEmail')
password=driver.find_element('id','logInPass')
username.send_keys('sanjay@joshi.com')
password.send_keys('Pass@1234')
login=driver.find_element('id','logInButton')
login.click()
time.sleep(2)
addresource=driver.find_element('id','AddResButton')
addresource.click()
time.sleep(1)
fName=driver.find_element(By.CSS_SELECTOR,"input[name=firstName]")
fName.send_keys("hello")
lName=driver.find_element('id','resLName')
lName.send_keys("Mello")
email=driver.find_element('id','resEmail')
email.send_keys("hello@mello.com")
contract=driver.find_element(By.ID,'contractType')
contract.click()
time.sleep(1)
skill=driver.find_element(By.CSS_SELECTOR,"div[class=MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-adornedEnd MuiAutocomplete-inputRoot css-1cr93ut]")
skill.click()
time.sleep(2)
option=driver.find_elements(By.CSS_SELECTOR,"li[tabindex=0]")
print('-------------------------------------------')
print(option)
print('-------------------------------------------')

option.click()
time.sleep(4)
univer=driver.find_element('id','resUniversity0-label')
univer.click()
time.sleep(4)

