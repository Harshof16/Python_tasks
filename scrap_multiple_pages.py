# scrap quotes across multiple pages and save the results to a CSV file using Python's csv module.

import requests
from bs4 import BeautifulSoup
import time
import csv
import os
import urllib.robotparser

# function to check if a URL can be fetched according to robots.txt
def can_fetch(url):
    """Check if the URL can be fetched according to robots.txt."""
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url + "robots.txt")
    rp.read()
    return rp.can_fetch("*", url)

base_url = "https://quotes.toscrape.com/page/{}/"
output_file = "quotes.csv"

# fetch quotes just from these authors
authors = ["J.K. Rowling", "James Baldwin", "Bob Marley", "Albert Einstein", "Mark Twain"]

# function to scrape quotes from a single page
def scrape_single_page(page_url):
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage, Status code: {response.status_code}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        # Check if the author is in the specified list
        if author not in authors:
            continue
        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
        writer.writerow([text, author, ', '.join(tags)])  # entry into csv file
        # Print the quote, author, and tags
        print(f"Quote: {text}\nAuthor: {author}\nTags: {', '.join(tags)}\n")
    return quotes

# open a CSV file to write the quotes
if os.path.exists(output_file):
    os.remove(output_file)  # remove the file if it already exists

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Quote', 'Author', 'Tags'])  # write the header row
    for page in range(1, 6):  # Scraping first 5 pages
        print(f"Scraping page {page}...")
        url = base_url.format(page)
        if not can_fetch(url):      # validates if the URL can be fetched
            # If the URL cannot be fetched according to robots.txt, skip it
            print(f"Cannot fetch {url} according to robots.txt")
            continue
        scrape_single_page(url)
        print(f"Finished scraping page {page}.\n")
        time.sleep(2)  # Sleep to avoid overwhelming the server

