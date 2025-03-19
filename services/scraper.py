from bs4 import BeautifulSoup
import requests
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to process an uploaded file
def scrape_file(file):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    return soup.title.string if soup.title else "No title found"

# Function to scrape a webpage from a URL
def scrape_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string if soup.title else "No title found"
    except Exception as e:
        return f"Error: {str(e)}"
