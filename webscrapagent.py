import requests
from bs4 import BeautifulSoup

class WebScraperAgent:
    def __init__(self):
        pass

    def scrape(self, query):
        search_url = f"https://www.example.com/search?q={query.replace(' ', '+')}"
        response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"})
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = [p.text for p in soup.find_all('p')]
            return results[:5]  # Return first 5 paragraphs
        else:
            return ["Failed to fetch data"]
