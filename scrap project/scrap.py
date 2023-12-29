from time import sleep
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

USERNAME = "tech_n_trickzz"
PASSWORD = "ankit@admin"

driver = webdriver.Chrome(executable_path='D:\pycharm\scrap project\chromedriver.exe')
driver.maximize_window()

insta_url = 'https://www.instagram.com/'
driver.get(insta_url)

sleep(1)

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
username_field.send_keys(USERNAME)

sleep(1)

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password_field.send_keys(PASSWORD)

sleep(1)

login_button = password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')))
login_button.click()

sleep(15)

driver.get(insta_url + 'akash_singh__1239')
sleep(5)

ul = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'ul')))
items = WebDriverWait(ul, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'li')))

for li in items:
    print(li.text)

sleep(59)

