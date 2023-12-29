import requests
from getpass import getpass
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


# Send an authenticated request to GitHub's API
response = requests.get(
    'https://api.github.com/user',
    auth=('ankit637', getpass())
)
print(response.json())  # This will print the JSON response from GitHub's API


# Send a request to httpbin.org with custom authentication
response = requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
print(response.json())  # This will print the JSON response from httpbin.org


