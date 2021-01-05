import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime

now = datetime.now()
today = now.strftime("%H%M%S")
date = now.strftime("%YYYY-%MM-%DD")
data_csv = "country-2021-01-05.csv"
driver = webdriver.Chrome('drivers/chromedriver.exe')
driver.get('https://amrs-dev.engkantar.com')
driver.maximize_window()
user = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, '//*[@id="login-form"]/fieldset/section[1]/label[2]/input')))
user.send_keys("testqa")
password = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/section[2]/label[2]/input')
password.send_keys("#testqa@")
submit = driver.find_element_by_xpath('//*[@id="login-form"]/footer/button')
submit.click()
time.sleep(2)
home = driver.find_element_by_xpath('//*[@id="left-panel"]/nav/ul/li[1]')
home.click()
countries = driver.find_element_by_xpath('//*[@id="left-panel"]/nav/ul/li[1]/ul/li[1]')
countries.click()
add_countries = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="countryTable_wrapper"]/div[2]/div[1]/a')))
add_countries.click()
edit_countries = driver.find_element_by_xpath('//*[@id="countryTable"]/tbody/tr[1]/td[1]/a[1]')
edit_countries.click()
add_country_id = driver.find_element_by_xpath(
    '//*[@id="countryTable"]/tbody/tr[1]/td[2]/span/div/form/div/div[1]/div/input')
add_country_id.send_keys(today)
select_country = driver.find_element_by_xpath('//*[@id="s2id_autogen1"]/ul')
select_country.click()
select_country = driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[77]')
select_country.click()
save_country = driver.find_element_by_xpath('//*[@id="countryTable"]/tbody/tr[1]/td[1]/a[3]/i')
save_country.click()
time.sleep(2)
delete_country = driver.find_element_by_xpath('//*[@id="countryTable"]/tbody/tr[1]/td[1]/a[4]')
delete_country.click()
time.sleep(2)
confirm_delete_contry = driver.find_element_by_xpath('//*[@id="save_btn"]')
confirm_delete_contry.click()
download_csv = driver.find_element_by_xpath('//*[@id="ToolTables_countryTable_0"]')
download_csv.click()

with open(data_csv, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if row[1] == today:
            if line_count == 0:
                line_count += 1
                if row[1] == "172720":
                    print("Correct assertion")
                else:
                    print("Error in file")
            line_count += 1
