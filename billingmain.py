from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import chromedriver_autoinstaller
import time 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get('http://103.248.14.25:12369/univerge/openStatistics')

time.sleep(4)

id_pass = 'Admin1234'

driver.find_element(By.ID,'username').send_keys(id_pass)
driver.find_element(By.ID,'Passwd').send_keys(id_pass)
driver.find_element(By.CSS_SELECTOR,'#login > div.loginbuttondiv > button > span').click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,'#navigation > li.report > a').click()
time.sleep(5)