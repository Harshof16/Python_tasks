# Scraping via api
# Task : fetches Github user data and save it to a file

# Steps
# 1. Takes a GitHub username as input.
# 2. Fetches the user's data from the GitHub API.
# 3. Saves the user's data to a CSV file.
# 4. Handles errors if the user does not exist or if there is an issue with the request.
# 5. Prints the user's data to the console.

import requests
import csv

# Ask the user for a GitHub username
username = input("Enter a GitHub username: ")

#Github API URL
url = f"https://api.github.com/users/{username}"

# Make a request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    user_data = response.json()

    keys = ["name", "bio", "public_repos", "followers", "following", "html_url"]
    name, bio, public_repos, followers, following, profile_url = (user_data.get(k) for k in keys)

    # Print info
    print(f"\nName: {name}")
    print(f"Bio: {bio}")
    print(f"Public Repos: {public_repos}")
    print(f"Followers: {followers}")
    print(f"Following: {following}")
    print(f"Profile URL: {profile_url}")

    #Save user data to a CSV file
    with open("githube_user_data.csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Bio", "Repos", "Followers", "Following", "URL"])
        writer.writerow([name, bio, public_repos, followers, following, profile_url])
    print("\nSaved user info to github_user.csv")
else:
    print(f"Error: User '{username}' not found or request failed with status code {response.status_code}")

