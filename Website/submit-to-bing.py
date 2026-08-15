"""
Bing IndexNow Submission Script
Run this script after uploading changes to GitHub to notify Bing instantly.
Usage: double-click this file, or run: python3 submit-to-bing.py
"""

import urllib.request
import json

API_KEY = "43492ce8376f47549a22c44107b17d77"
HOST = "www.caitlindaprano.com"

URLS = [
    "https://www.caitlindaprano.com/",
    "https://www.caitlindaprano.com/about.html",
    "https://www.caitlindaprano.com/testimonials.html",
    "https://www.caitlindaprano.com/contact.html",
    "https://www.caitlindaprano.com/blog/index.html",
    "https://www.caitlindaprano.com/blog/sf-real-estate-neighborhood-guide.html",
]

payload = json.dumps({
    "host": HOST,
    "key": API_KEY,
    "keyLocation": f"https://{HOST}/{API_KEY}.txt",
    "urlList": URLS
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.indexnow.org/IndexNow",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        print(f"✅ Success! Bing notified. Status: {response.status}")
        print(f"   {len(URLS)} URLs submitted.")
except Exception as e:
    print(f"❌ Error: {e}")

input("\nPress Enter to close...")
