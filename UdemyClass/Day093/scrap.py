# Testing Copilot generation

import requests
from bs4 import BeautifulSoup
import csv

# Add headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}

# List of job hunting article URLs
URLS = [
    "https://www.indeed.com/career-advice/finding-a-job/job-hunting",
    "https://www.metaintro.com/blog/job-hunting-strategies",
    "https://careersidekick.com/job-search-tips/"
]

def scrape_article(url):
    """Scrape title and description from a given URL."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # raise error for bad status codes
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title safely
        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True) if title_tag else "No title found"

        # Extract meta description safely
        desc_tag = soup.find("meta", attrs={"name": "description"})
        description = desc_tag["content"].strip() if desc_tag and "content" in desc_tag.attrs else "No description available"

        return {"title": title, "url": url, "description": description}

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return {"title": "Error", "url": url, "description": str(e)}

def save_to_csv(data, filename="job_hunting_articles.csv"):
    """Save scraped data to CSV."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "description"])
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV file created: {filename}")

def main():
    articles = []
    for url in URLS:
        article = scrape_article(url)
        articles.append(article)

    save_to_csv(articles)

if __name__ == "__main__":
    main()
