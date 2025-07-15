# Task: Fetches multiple repositories of a GitHub user with authentication and pagination

# Steps
# 1. Takes a GitHub username and token as input.
# 2. Fetches the user's repositories from the GitHub API with pagination.
# 3. Handles errors if the user does not exist or if there is an issue with the request.
# 4. Continues fetching until all repositories are retrieved.
# 5. Prints the total number of repositories fetched.
# 6. Saves the repository data to a CSV file.
# 7. Handles rate limiting by checking the response headers.

import requests
import csv

username = input("Enter a GitHub username: ")
token = input("Enter your GitHub token: ")

# Base URL for the GitHub API
url = f"https://api.github.com/users/{username}/repos"
headers = {"Authorization": f"token {token}"}

# constants for pagination
per_page = 5  # Number of repositories per page
page = 1  # Start from the first page

repos = [] # list to store all repositories

while True:
    response = requests.get(url, headers=headers, params={"per_page": per_page, "page": page})

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        print(response.json())
        break

    data = response.json()
    if not data:
        break
    
    repos.extend(data)  # Add the current page of repositories to the list
    page += 1  # Move to the next page

print(f"\nTotal repositories fetched: {len(repos)}")

# Save the repository data to a CSV file
if repos:       # saving only when data is there in the repos list
    with open("github_repos.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Description", "Stars", "Forks", "Language", "URL", "Created At", "Last Modified"])
        for repo in sorted(repos, key=lambda x: x['updated_at'], reverse=True):  # Sort by last modified date
            name = repo.get("name") # Get the repository name, get is method of dict
            description = repo.get("description", "No description")
            stars = repo.get("stargazers_count", 0)
            forks = repo.get("forks_count", 0)
            language = repo.get("language", "Not specified")
            url = repo.get("html_url")
            created_at = repo.get("created_at", "Not specified")
            last_modified = repo.get("updated_at", "Not specified")
            writer.writerow([name, description, stars, forks, language, url, created_at, last_modified])

# Save no. of repositories per year
if repos :
    with open("github_repos_per_year.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Year", "Number of Repositories"])
        year_count = {}
        for repo in repos:
            year = repo['created_at'][:4]
            if year in year_count:
                year_count[year] += 1
            else:
                year_count[year] = 1
        for year, count in sorted(year_count.items()):
            writer.writerow([year, count])
    print("\nSaved repository data to github_repos.csv")

