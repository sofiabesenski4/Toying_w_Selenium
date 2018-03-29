#selenium_testing.py
from selenium import webdriver
import time
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome("/home/teb8/School/Research/Chromedriver/chromedriver", chrome_options = chrome_options)
driver.get('http://demo.guru99.com/test/flash-testing.html')
time.sleep(2)
#driver.execute_script("document.body.style.zoom='1.5'")
time.sleep(5)
flash_box = driver.find_element_by_id('myFlashMovie')
row = driver.find_element_by_class_name('row')
#flash_box.click()
#search_box.send_keys('ChromeDriver')
#search_box.submit()
actions = ActionChains(driver)
actions.move_to_element_with_offset(flash_box,50,-50)

actions.click()
actions.perform()
time.sleep(2) # Let the user actually see something!
actions = ActionChains(driver)
actions.move_to_element_with_offset(row,350,20)
actions.click()
actions.perform()
time.sleep(2)
print(Alert(driver).text)
"""
actions = ActionChains(driver)
actions.send_keys(Keys.TAB + Keys.TAB +Keys.ENTER)
actions.perform()
time.sleep(5)
"""
driver.quit()


