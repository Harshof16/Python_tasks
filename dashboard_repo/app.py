from flask import Flask, request, render_template
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/repos"

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        return fetch_profile(username)
    return render_template("index.html")

def fetch_profile(username):
    url = GITHUB_API_URL.format(username)
    response = requests.get(url)

    if response.status_code != 200:
        return render_template("profile.html", error="User not found.")
    
    repos = response.json()
    total_stars = sum(repo["stargazers_count"] for repo in repos)
    total_forks = sum(repo["forks_count"] for repo in repos)

    # Explanation of each term:
    # - key=lambda r: r["stargazers_count"]: a function that tells sorted() to use the "stargazers_count" value
    #   from each repository dictionary 'r' as the sorting key.
    # - reverse=True: sorts the list in descending order (highest stars first).
    # - [:5]: slices the sorted list to get only the first 5 items (the top 5 most-starred repositories).
    top_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]

    return render_template("profile.html", username=username, total_repos=len(repos),  total_stars=total_stars,
                           total_forks=total_forks,
                           top_repos=top_repos)

if __name__ == "__main__":
    app.run(debug=True)