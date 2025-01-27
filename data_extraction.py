import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the URL: {url}")

def extract_relevant_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find_all('p') 
    return [item.text.strip() for item in data]
