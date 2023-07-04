from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
import time 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get('http://103.248.14.25:12369/univerge/openStatistics')



id_pass = 'Admin1234'
wait = WebDriverWait(driver,10)

# logging into uniVerge
wait.until(EC.visibility_of_element_located((By.ID,'username'))).send_keys(id_pass)
wait.until(EC.visibility_of_element_located((By.ID,'Passwd'))).send_keys(id_pass)
driver.find_element(By.CSS_SELECTOR,'#login > div.loginbuttondiv > button > span').click()

# Report Tab seletion
wait.until(EC.invisibility_of_element_located((By.ID, 'overlay')))
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navigation"]/li[4]/a'))).click()


# Daily Report Tab seletion
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dailyReportForICX"]/a'))).click()

# selection of date and time
driver.find_element(By.ID,'startDateTime').clear()
driver.find_element(By.ID,'startDateTime').send_keys('2023-07-03 00:00:00')
driver.find_element(By.ID,'endDateTime').clear()
driver.find_element(By.ID,'endDateTime').send_keys('2023-07-03 23:59:59')

# seletion of 'Client type' (IOS)
dropdown_element = driver.find_element(By.ID, "clienttype_chzn")
dropdown_element.click()

driver.find_element(By.ID,'clienttype_chzn_o_1').click()

# downloading the report IOS => Incomming
driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[4]/button[3]').click()


# seletion of 'Client type' (ANS)
dropdown_element = driver.find_element(By.ID, "clienttype_chzn")
dropdown_element.click()

driver.find_element(By.ID,'clienttype_chzn_o_2').click()


# seletion of 'Call Type' (Outgoing)
dropdown_element = driver.find_element(By.ID, "calltype_chzn")
dropdown_element.click()

driver.find_element(By.ID,'calltype_chzn_o_1').click()


# downloading the report ANS => outgoing
driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[4]/button[3]').click()




time.sleep(40)
