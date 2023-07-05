from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

id_pass = 'Admin1234'
date = input('Enter date (e.g., \'2023-01-01\'):')
url = 'http://103.248.14.25:12369/univerge/openStatistics'

driver.get(url)
wait = WebDriverWait(driver, 10)


def login_and_select_report():
    wait.until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys(id_pass)
    wait.until(EC.visibility_of_element_located((By.ID, 'Passwd'))).send_keys(id_pass)
    driver.find_element(By.CSS_SELECTOR, '#login > div.loginbuttondiv > button > span').click()

    wait.until(EC.invisibility_of_element_located((By.ID, 'overlay')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navigation"]/li[4]/a'))).click()


def select_date_time(start_date_time, end_date_time):
    driver.find_element(By.ID, 'startDateTime').clear()
    driver.find_element(By.ID, 'startDateTime').send_keys(start_date_time)
    driver.find_element(By.ID, 'endDateTime').clear()
    driver.find_element(By.ID, 'endDateTime').send_keys(end_date_time)


def select_dropdown_option(dropdown_id, option_id):
    dropdown_element = driver.find_element(By.ID, dropdown_id)
    dropdown_element.click()
    driver.find_element(By.ID, option_id).click()


def download_report(xpath):
    driver.find_element(By.XPATH,xpath).click()


# Logging in and selecting the report tab
login_and_select_report()

# Daily Report Tab
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dailyReportForICX"]/a'))).click()

# Selecting date and time
select_date_time(f'{date} 00:00:00', f'{date} 23:59:59')

# Selecting 'Client type' (IOS) and downloading the report
select_dropdown_option('clienttype_chzn', 'clienttype_chzn_o_1')
download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[4]/button[3]')
print('International Incomming Report downloaded')

# Selecting 'Client type' (ANS)
select_dropdown_option('clienttype_chzn', 'clienttype_chzn_o_2')

# Selecting 'Call Type' (Outgoing) and downloading the report
select_dropdown_option('calltype_chzn', 'calltype_chzn_o_1')
download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[4]/button[3]')
print('International Outgoing Report(ANS wise) downloaded')

# POPwise Report Tab
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popeWiseReportICX"]/a'))).click()

# Selecting date and time
select_date_time(f'{date} 00:00:00', f'{date} 23:59:59')

# Downloading the reports for DHK, CTG, and SYL
for city, option_id in {'DHK': 'calltype_chzn_o_1', 'CTG': 'calltype_chzn_o_0', 'SYL': 'calltype_chzn_o_2'}.items():
    select_dropdown_option('calltype_chzn', option_id)
    download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[3]/button/span')
    print(f'POPwise Report downloaded:{city}')

# Call Volume By IGW Report Tab
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="callvolumereportigwForICX"]/a'))).click()

# Selecting date and time
select_date_time(f'{date} 00:00:00', f'{date} 23:59:59')

# Selecting call type Outgoing and report type Outgoing, and downloading the report
select_dropdown_option('calltype_chzn', 'calltype_chzn_o_1')
select_dropdown_option('reporttype_chzn', 'reporttype_chzn_o_3')
download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/div[4]/button/span')
print('International Outgoing Report(IGW wise) downloaded')

time.sleep(5)
driver.quit()
