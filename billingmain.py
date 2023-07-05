from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
import time 

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()


id_pass = 'Admin1234'
date =input('Enter date (exp:\'2023-01-01\'):')

url ='http://103.248.14.25:12369/univerge/openStatistics'

driver.get(url)

wait = WebDriverWait(driver,10)

# logging into uniVerge
wait.until(EC.visibility_of_element_located((By.ID,'username'))).send_keys(id_pass)
wait.until(EC.visibility_of_element_located((By.ID,'Passwd'))).send_keys(id_pass)
driver.find_element(By.CSS_SELECTOR,'#login > div.loginbuttondiv > button > span').click()

# Report Tab seletion
wait.until(EC.invisibility_of_element_located((By.ID, 'overlay')))
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navigation"]/li[4]/a'))).click()

#-------------------------------------xoxoxoxoxox-----------------------------------------------------------
# Daily Report Tab seletion
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dailyReportForICX"]/a'))).click()

# selection of date and time
driver.find_element(By.ID,'startDateTime').clear()
driver.find_element(By.ID,'startDateTime').send_keys(f'{date} 00:00:00')
driver.find_element(By.ID,'endDateTime').clear()
driver.find_element(By.ID,'endDateTime').send_keys(f'{date} 23:59:59')

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



#---------------------------------------POPwise Report-----------------------------------------------------------
# POPwise Report Tab seletion
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="popeWiseReportICX"]/a'))).click()

# selection of date and time
driver.find_element(By.ID,'startDateTime').clear()
driver.find_element(By.ID,'startDateTime').send_keys(f'{date} 00:00:00')
driver.find_element(By.ID,'endDateTime').clear()
driver.find_element(By.ID,'endDateTime').send_keys(f'{date} 23:59:59')

# downloading the report => DHK
dropdown_element = driver.find_element(By.ID,"calltype_chzn")
dropdown_element.click()
driver.find_element(By.ID,'calltype_chzn_o_1').click()

driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[3]/button/span').click()



# downloading the report => CTG
dropdown_element = driver.find_element(By.ID,"calltype_chzn")
dropdown_element.click()
driver.find_element(By.ID,'calltype_chzn_o_0').click()

driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[3]/button/span').click()

# downloading the report => SYL
dropdown_element = driver.find_element(By.ID,"calltype_chzn")
dropdown_element.click()
driver.find_element(By.ID,'calltype_chzn_o_2').click()

driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[3]/button/span').click()



#---------------------------------------Volume By IGW Report-----------------------------------------------------------
# Call Volume By IGW Report Tab seletion
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="callvolumereportigwForICX"]/a'))).click()

# selection of date and time
driver.find_element(By.ID,'startDateTime').clear()
driver.find_element(By.ID,'startDateTime').send_keys(f'{date} 00:00:00')
driver.find_element(By.ID,'endDateTime').clear()
driver.find_element(By.ID,'endDateTime').send_keys(f'{date} 23:59:59')

# selecting call type Outgoing
dropdown_element = driver.find_element(By.ID,"calltype_chzn")
dropdown_element.click()
driver.find_element(By.ID,'calltype_chzn_o_1').click()

# selecting Report Type Outgoing
dropdown_element = driver.find_element(By.ID,"reporttype_chzn")
dropdown_element.click()
driver.find_element(By.ID,'reporttype_chzn_o_3').click()


# downloading the report 
driver.find_element(By.XPATH,'/html/body/div[1]/table/tbody/tr[2]/td[2]/div/div[4]/button/span').click()

time.sleep(5)
driver.quit()
