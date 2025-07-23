# Task :
# A simple, clean Flask app that:
# Loads your cleaned_repos.csv file
# Displays a summary dashboard:
# 📊 Total repos, total stars, forks
# 📌 Top 5 most-starred repos
# 📈 Bar chart: stars per repo
# Uses Jinja2 templates + chartjs

from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)   # initalize the app

@app.route("/")     # route for the homepage
def index():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "github_repos.csv")
    df = pd.read_csv(csv_path)

    total_repos = len(df)
    total_stars = df['Stars'].sum()
    total_forks = df['Forks'].sum()
    top_repos = df.sort_values(by='Stars', ascending=False).head(5)

    # For chart
    chart_data = top_repos[['Name','Stars']].values.tolist()

    return render_template("index.html", total_repos=total_repos,
                           total_stars=total_stars,
                           total_forks=total_forks,
                           top_repos=top_repos,
                           chart_data=chart_data)

if __name__ == "__main__":
    app.run(debug=True)        # Enables auto-reload + error messages

