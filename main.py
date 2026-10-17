
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://books.toscrape.com/"


def fetch_page(url):
    """Download the webpage HTML."""
    try:
        response = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "CodeAlpha-WebScraping-Student/1.0"}
        )
        response.raise_for_status()
        return response.text

    except requests.RequestException as error:
        print(f"Error downloading webpage: {error}")
        return None


def scrape_books(html):
    """Extract book details from the webpage."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a.get("title", "Unknown")
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)

        rating_element = book.select_one(".star-rating")
        rating = (
            rating_element.get("class", ["", "Unknown"])[1]
            if rating_element and len(rating_element.get("class", [])) > 1
            else "Unknown"
        )

        relative_url = book.h3.a.get("href", "")
        product_url = urljoin(URL, relative_url)

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })

    return books


def main():
    html = fetch_page(URL)

    if html is None:
        print("Scraping stopped because the webpage could not be downloaded.")
        return

    books = scrape_books(html)

    if not books:
        print("No books were found. Please check the webpage structure.")
        return

    df = pd.DataFrame(books)

    # Fix the pound symbol if it was incorrectly decoded.
    df["Price"] = df["Price"].str.replace("Â£", "£", regex=False)

    output_file = "books_dataset.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"\nSuccessfully scraped {len(df)} books.")
    print(f"Dataset saved to: {output_file}")
    print("\nSample records:")
    print(df.head().to_string(index=False))


if __name__ == "__main__":
    main()
