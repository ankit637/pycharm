from bs4 import BeautifulSoup
import requests

def extract_soup_parameters(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None
    else:
        print('Success!')
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract parameters from the soup object here
        # For example, extracting all the 'href' attributes from anchor tags
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # You can add more extraction logic here based on what you need

        return links  # Return the extracted parameters or data

# Example usage:
url_to_scrape = 'https://www.studyiq.com/'  # Replace with your desired URL
extracted_links = extract_soup_parameters(url_to_scrape)
if extracted_links:
    for link in extracted_links:
        print(link)
