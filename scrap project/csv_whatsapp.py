import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Path to the CSV file containing contact numbers
csv_file = 'data.csv'

# Path to the WebDriver executable (e.g., chromedriver for Chrome)
webdriver_path = 'D:\pycharm\scrap project\chromedriver.exe'

# ...

# Function to send WhatsApp message
def send_whatsapp_message(contact, message):
    # Launch the browser
    driver = webdriver.Chrome(webdriver_path)  # Change to the appropriate WebDriver

    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com')
    sleep(10)  # Adjust the sleep duration based on your internet speed and system performance

    # Search for the contact
    search_box = driver.find_element(By.CLASS_NAME, 'copyable-text selectable-text')
    search_box.click()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    sleep(5)

    # Send the message
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    sleep(2)

    # Close the browser
    driver.quit()

# ...


# Read the contact numbers from the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        contact_number = row[0]
        message = "Hello, this is a WhatsApp message sent using Python!"
        send_whatsapp_message(contact_number, message)
        print(f"Message sent to {contact_number}")

print("All messages sent successfully!")
