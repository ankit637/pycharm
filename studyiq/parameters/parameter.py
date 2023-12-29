import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import re
import json

url = 'https://www.studyiq.com/'

try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

    # ... (previous code)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Check if links are found before attempting to find parameters
    if links:
        url_params = re.findall(r'\?.*?(?=#|$)', ' '.join(links))

        with open('url_parameters.txt', 'w') as params_file:
            for params in url_params:
                params_file.write(params + '\n')
    else:
        print('No links found.')
    print(links)

    # ... (rest of the code)

