import requests  # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import pandas as pd  # Import Pandas for data manipulation and analysis

# Specify the URL of the website to scrape
url = 'https://notes.ayushsharma.in/technology'

# Send an HTTP GET request to the specified URL and store the response
data = requests.get(url)

# Create an empty list to store the extracted data
my_data = []

# Parse the HTML content of the page using BeautifulSoup
html = BeautifulSoup(data.text, 'html.parser')

# Select all elements with the class 'post-card' using CSS selectors
articles = html.select('a.post-card')

# Iterate over each 'post-card' element to extract information
for article in articles:
    # Extract the title of the article
    title = article.select('.card-title')[0].get_text()

    # Extract the excerpt of the article
    excerpt = article.select('.card-text')[0].get_text()

    # Extract the publication date of the article
    pub_date = article.select('.card-footer small')[0].get_text()

    # Append the extracted data to the list as a dictionary
    my_data.append({"Title": title, "Excerpt": excerpt, "Pub_Date": pub_date})

# Create a Pandas DataFrame from the extracted data with specified column headings
df = pd.DataFrame(my_data, columns=["Title", "Excerpt", "Pub_Date"])

# Write the DataFrame to a CSV file named 'output_with_headings.csv' without index column
df.to_csv('output_with_headings.csv', index=False)

# Print a message indicating that the data has been written to the CSV file
print("Data written to 'output_with_headings.csv'")
