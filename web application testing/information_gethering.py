'''
    Information Gathering:

Use Python libraries like requests or urllib to interact with the target web application and gather information about
 its structure, functionality, and technology stack.
Example: Send an HTTP request to a URL and retrieve the response:
'''

import requests

url = 'https://kakacric.com/login'
response = requests.get(url)
print(response.text)
