import requests
from bs4 import BeautifulSoup
import pandas as pd

print("✅ Your environment is working!")

# Example: fetch title from a webpage
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Page title:", soup.title.string)
