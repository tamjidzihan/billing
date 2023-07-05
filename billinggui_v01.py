from tkinter import messagebox
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk
import chromedriver_autoinstaller
import datetime


def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


chromedriver_autoinstaller.install()
chrome_options = Options()

id_pass = 'Admin1234'
url = 'http://103.248.14.25:12369/univerge/openStatistics'

# Create the main window
window = tk.Tk()
window.title("Billing Report Downloader")


# Load the logo image
logo_path = "./tele_exchange_limited_logo.jpg"
logo_image = Image.open(logo_path)
logo_width, logo_height = 200, 100  # Set the desired width and height for the logo
logo_image.thumbnail((logo_width, logo_height))
logo_image = ImageTk.PhotoImage(logo_image)

# Create a label for the logo
logo_label = tk.Label(window, image=logo_image)
logo_label.pack()


# Set the window dimensions and center it on the screen
window_width = 600
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_pos = (screen_width / 2) - (window_width / 2)
y_pos = (screen_height / 2) - (window_height / 2)
window.geometry(f"{window_width}x{window_height}+{int(x_pos)}+{int(y_pos)}")

# Create input fields
date_label = tk.Label(window, text="Enter date (e.g., '2023-01-01'): ")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

# Create a text area to display the update reports
report_label = tk.Label(window, text="Status :")
report_label.pack()
reports_text = tk.Text(window, height=10, width=60)
reports_text.pack()


def show_message_box(title, message):
    messagebox.showinfo(title, message)


def download_reports():
    date = date_entry.get()

    if not validate_date(date):
        show_message_box("Invalid Date", "Please enter a valid date in the format 'YYYY-MM-DD'.")
        return

    driver = webdriver.Chrome()
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
        driver.find_element(By.XPATH, xpath).click()

    def update_reports_text(message):
        reports_text.insert(tk.END, message + "\n")
        reports_text.see(tk.END)  # Scroll to the latest message
        window.update()  # Update the GUI

    try:
        # Logging in and selecting the report tab
        login_and_select_report()
        update_reports_text('Logging in....')

        # Daily Report Tab
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dailyReportForICX"]/a'))).click()

        # Selecting date and time
        select_date_time(f'{date} 00:00:00', f'{date} 23:59:59')

        # Selecting 'Client type' (IOS) and downloading the report
        update_reports_text('Downloading International Incoming Report')
        select_dropdown_option('clienttype_chzn', 'clienttype_chzn_o_1')
        download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[4]/button[3]')
        update_reports_text('International Incoming Report downloaded')

        # Selecting 'Client type' (ANS)
        select_dropdown_option('clienttype_chzn', 'clienttype_chzn_o_2')

        # Selecting 'Call Type' (Outgoing) and downloading the report
        update_reports_text('Downloading International Outgoing Report(ANSwise) Report')
        select_dropdown_option('calltype_chzn', 'calltype_chzn_o_1')
        download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[4]/button[3]')
        update_reports_text('International Outgoing Report(ANS wise) downloaded')

        # POPwise Report Tab
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popeWiseReportICX"]/a'))).click()

        # Selecting date and time
        select_date_time(f'{date} 00:00:00', f'{date} 23:59:59')

        # Downloading the reports for DHK, CTG, and SYL
        for city, option_id in {'DHK': 'calltype_chzn_o_1', 'CTG': 'calltype_chzn_o_0', 'SYL': 'calltype_chzn_o_2'}.items():
            update_reports_text(f'Downloading POPwise Report: {city}')
            select_dropdown_option('calltype_chzn', option_id)
            download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div[1]/div[3]/button/span')
            update_reports_text(f'POPwise Report downloaded: {city}')

        # Call Volume By IGW Report Tab
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="callvolumereportigwForICX"]/a'))).click()

        # Selecting date and time
        select_date_time(f'{date} 00:00:00', f'{date} 23:59:59')

        # Selecting call type Outgoing and report type Outgoing, and downloading the report
        update_reports_text('Downloading International Outgoing Report(IGW wise) Report')
        select_dropdown_option('calltype_chzn', 'calltype_chzn_o_1')
        select_dropdown_option('reporttype_chzn', 'reporttype_chzn_o_3')
        download_report('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/div[4]/button/span')
        update_reports_text('International Outgoing Report(IGW wise) downloaded')

        show_message_box("Reports Downloaded", "All reports have been downloaded successfully.")
    except Exception as e:
        show_message_box("Error", f"An error occurred:\n{str(e)}")
    finally:
        driver.quit()


def exit_application():
    if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
        window.destroy()


# Create the download button
download_button = tk.Button(window, text="Download Reports", command=download_reports)
download_button.pack()

# Create the exit button
exit_button = tk.Button(window, text="Exit", command=exit_application)
exit_button.pack()

# Start the GUI main loop
window.mainloop()
