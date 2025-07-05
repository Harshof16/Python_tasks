# Task : Fetch latest headlines from a news API, and if the headline mentions “AI”, send a message on email (need SMTP) or Whatasapp (twilio).

# Steps
#  1. Fetch top headlines from NewsAPI
#  2. Filter articles based on keywords (e.g., "AI")
#  3. Send alert via Email (recommended) or WhatsApp

import os
import re
import requests
from utils import format_date
from dotenv import load_dotenv
from email_msg import send_email
from twilio_msg import send_whatsapp_message

#Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_ai_headlines():
   url = "https://newsapi.org/v2/everything"
   params = {
        "q": "AI",
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10  # Fetch only the top 10 articles
   }
   response = requests.get(url, params=params)
   data = response.json()

   if data.get("status") != "ok":
         print("Error fetching news")
         return []

   # Filter articles that mention "AI" in the title or description
   # Use regex to match 'AI' as a separate word (case-insensitive)
   pattern = re.compile(r'\bAI\b', re.IGNORECASE)
   return [
        f"{article['title']} - {format_date(article['publishedAt'] or "")}\n{article['url']}"
        for article in data.get("articles", [])
        if pattern.search(article.get("title", "") or "") or pattern.search(article.get("description", "") or "")
   ]

headlines = fetch_ai_headlines()

if headlines:
    # Send email with AI-related headlines
    email_body = "\n\n".join(headlines)
    send_email("🔥 AI News Update", email_body)
    # Send WhatsApp message
    whatsapp_message = "🔥 AI News Update:\n\n" + "\n\n".join(headlines)
    send_whatsapp_message(whatsapp_message)
    print("AI-related headlines sent via email:")
    # Print the headlines to console
    for headline in headlines:
        print(f"Heading {headlines.index(headline) + 1} : {headline}")
else:
    print("No AI-related headlines found.") 


# Explanation of the code:
# if pattern.search(article.get("title", "") or "") or pattern.search(article.get("description", "") or "")

# article.get("title", "")
# This tries to get the value of the "title" key from the article dictionary.
# If "title" does not exist, it returns an empty string "".
# or ""
# This ensures that if the value from article.get("title", "") is falsy (like None or ""), it defaults to an empty string.
# This is a defensive coding pattern to avoid passing None to the regex search, which expects a string.
# pattern.search(...)
# pattern is a compiled regular expression object.
# .search(string) scans through the string, looking for any location where the regex pattern matches.
# Returns a match object if found, otherwise None.
# or (logical OR)
# The condition checks if either the title or the description matches the pattern.
# If either pattern.search(...) call returns a match object (which is truthy), the whole condition is True.
# article.get("description", "") or ""
# Same logic as for "title", but for the "description" key.

{'source': {'id': 'the-verge', 'name': 'The Verge'}, 'author': 'Mia Sato', 'title': 'Here comes the AI sponcon', 'description': 'Social media is filled with an endless supply of people selling things, from Shein try-on hauls to health supplement and gadget product placements. Influencer marketing disrupted traditional advertising, creating an army of living room salespeople pumping out…', 'url': 'https://www.theverge.com/news/684572/tiktok-ai-advertising-videos-try-on-product-placement', 'urlToImage': 'https://platform.theverge.com/wp-content/uploads/sites/2/2025/06/Screenshot-2025-06-13-at-1.52.21%E2%80%AFPM.png?quality=90&strip=all&crop=0%2C6.6153534721519%2C100%2C86.769293055696&w=1200', 'publishedAt': '2025-06-14T22:15:34Z', 'content': 'TikTok will let brands generate AI influencer content that mimics what human creators might share.\r\nSocial media is filled with an endless supply of people selling things, from Shein try-on hauls to … [+3052 chars]'}