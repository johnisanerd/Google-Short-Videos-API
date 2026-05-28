"""
Google Short Videos API: A Quick Start Example
See more at: https://apify.com/johnvc/google-short-videos-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-short-videos-api/input-schema?fpr=9n7kx3

This script shows how to call the Google Short Videos API on Apify from Python and
read its structured JSON output. It returns short-form videos (YouTube Shorts,
Reels, TikTok, and more) for a search query, plus a related "people also search for"
list. It exercises several input parameters so you can see what is configurable,
while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query, max_pages=1) to keep this first run inexpensive.
# Raise these once you have your own API key and know your budget.
run_input = {
    "q": "workout tips",      # the search query (required)
    "device": "mobile",       # mobile or tablet also return "people also search for"
    "gl": "us",               # two-letter country code
    "hl": "en",               # two-letter interface language code
    "safe": "off",            # "active" filters explicit content, "off" does not
    "max_pages": 1,           # kept at 1 to keep this first run cheap (each page ~10 videos)
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-short-videos-api").call(run_input=run_input)

# Read structured results from the run's default dataset
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

# Each item is a flat row tagged with result_type: "short_video" or "people_also_search_for".
videos = [i for i in items if i.get("result_type") == "short_video"]
related = [i for i in items if i.get("result_type") == "people_also_search_for"]

print(f"Returned {len(items)} row(s): {len(videos)} short videos, {len(related)} related searches.\n")

for v in videos:
    print(f"[{v.get('position')}] {v.get('title')}")
    print(f"    source: {v.get('source')}  channel: {v.get('channel')}  duration: {v.get('duration')}")
    print(f"    link:   {v.get('link')}")

if related:
    print("\nPeople also search for:")
    for r in related:
        print(f"  - {r.get('title')}")
