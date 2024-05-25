import requests
from bs4 import BeautifulSoup
import random

# URL of the website you want to scrape
url = 'https://www.collegepravesh.com/articles/jee-advanced-2023-rank-vs-marks/'

# List of user agents to rotate
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
]

# Choose a random user agent
headers = {
    'User-Agent': random.choice(user_agents)
}

# Proxies dictionary with a valid proxy
proxies = {
    'http': 'http://your_proxy:port',
    'https': 'https://your_proxy:port',
}

# Use a session to persist certain parameters across requests
session = requests.Session()
session.headers.update(headers)

# Send a GET request to the URL with headers and proxies
response = session.get(url, proxies=proxies)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content of the page
    html_content = response.text
    
    # Optionally, parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Print the HTML content
    print(soup.prettify())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
