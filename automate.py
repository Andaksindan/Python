import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for IMDB's top 100 movies
url = 'https://www.imdb.com/chart/top'

# Send a GET request to the URL and get the page content
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find the table containing the movie information
table = soup.find('table', {'class': 'chart full-width'})

# Extract the movie names and years from the table
movies = []
for row in table.find_all('tr')[1:101]:  # Exclude the header row and limit to top 100 movies
    title_column = row.find('td', {'class': 'titleColumn'})
    name = title_column.find('a').text
    year = title_column.find('span', {'class': 'secondaryInfo'}).text.strip('()')
    movies.append((name, year))

# Create a pandas DataFrame with the movie data
df = pd.DataFrame(movies, columns=['Name', 'Year'])

# Save the DataFrame to an Excel file
df.to_excel('top_100_movies.xlsx', index=False)
