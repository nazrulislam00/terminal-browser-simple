import requests
from bs4 import BeautifulSoup

url = input("Enter URL: ")
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

print(text[:2000])
