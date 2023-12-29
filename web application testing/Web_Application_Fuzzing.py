'''
    Web Application Fuzzing:

Implement a Python script to perform fuzzing on various inputs of the web application, targeting common vulnerabilities
 like SQL injection or XSS.
Example: Generating a payload for SQL injection using Python:
'''
import urllib.parse

payload = "1' OR '1'='1"
encoded_payload = urllib.parse.quote(payload)
print(encoded_payload)
