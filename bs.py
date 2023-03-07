# Import the necessary libraries
from bs4 import BeautifulSoup
import requests

# Make a request to the website
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Extract information from the HTML
title = soup.title.string
first_paragraph = soup.find('p').text
all_links = [link.get('href') for link in soup.find_all('a')]

# Print the results
print('Title:', title)
print('First paragraph:', first_paragraph)
print('All links:', all_links)
