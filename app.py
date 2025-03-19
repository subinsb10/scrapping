from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


# Handle file upload and scrape its content
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    return f"Extracted Title: {soup.title.string}" if soup.title else "No title found"


# Scrape a webpage from a given URL
@app.route("/scrape", methods=["POST"])
def scrape_url():
    url = request.form.get("url")
    if not url:
        return "URL is required", 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        return f"Extracted Title: {soup.title.string}" if soup.title else "No title found"
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)

