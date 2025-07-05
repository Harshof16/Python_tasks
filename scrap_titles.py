# Task: Scrape titles from a webpage and save them to a file

# Steps:
# 1. install required libraries (requests, beautifulsoup4)
# 2. Fetch the webpage content using requests
# 3. Parse the content using BeautifulSoup
# 4. Extract titles from the parsed content

import requests
from bs4 import BeautifulSoup

# Fetching the webpage content
url = "https://www.python.org/blogs/"
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# parsing the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting blog titles from the webpage
ul = soup.find('ul', class_='list-recent-posts menu')

# Print blog titles
if not ul:
    print("Could not find the recent posts list.")
else:
    # Find all <li> children (one per post)
    posts = ul.find_all("li")
    for li in posts:
        a = li.find("a")
        title = a.text.strip()
        link = a.get("href")
        time = li.find("time")
        if time:
            time = time.get("datetime")
        else:
            time = "No date available"
        print(title, "| Date Posted :",time, "|| URL:", link)

