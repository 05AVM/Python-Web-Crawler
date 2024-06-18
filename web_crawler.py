import requests
from bs4 import BeautifulSoup
import csv

def fetch_urls(primary_category, secondary_category,):
    # Construct the search URL based on primary and secondary categories
    search_url = f"https://www.sanfoundry.com/{primary_category}/{secondary_category.replace(' ', '-').lower()}/"

    # Headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make a GET request to fetch the search results page
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract URLs from the search results
        urls = []
        for article in soup.find_all('div', class_='entry-content'):
            link = article.find('a', href=True)
            if link:
                urls.append(link['href'])

        # Write URLs to a CSV file
        output_file = 'output_urls.csv'
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['URL', 'Primary Category', 'Secondary Category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for url in urls:
                writer.writerow({'URL': url, 'Primary Category': primary_category,
                                 'Secondary Category': secondary_category})
        print(f"URLs extracted and saved to {output_file}")

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Example input parameters
    parameters = {
        "Primary Category": "tutorials",
        "Secondary Category": "C Tutorials",
        "Geography": "India",
        "Date Range": "2022-23"
    }

    # Fetch URLs using the parameters
    fetch_urls(parameters["Primary Category"], parameters["Secondary Category"],parameters["Geography"],parameters['Date Range'])
