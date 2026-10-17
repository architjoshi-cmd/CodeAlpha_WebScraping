# CodeAlpha Web Scraping Project

## Project Overview
This project demonstrates web scraping using Python to extract structured book information from [Books to Scrape](https://books.toscrape.com/), a website designed for scraping practice.

## Objectives
- Retrieve webpage content using Python.
- Parse HTML and extract book information.
- Store the collected data in a CSV file.
- Validate the dataset for missing values and duplicate records.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Visual Studio Code

## Data Collected
The scraper extracts the following fields:
- **Title:** Book title
- **Price:** Listed book price
- **Rating:** Book rating
- **Availability:** Stock availability
- **Product URL:** Link to the individual book page

The current run collected 20 book records from the website's first page.

## Project Files
- `main.py` — Web scraping script
- `books_dataset.csv` — Scraped dataset
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation

## Installation and Usage

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment if needed.
4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Run the scraper:

   ```bash
   python main.py
   ```

The script saves the extracted data to `books_dataset.csv`.

## Validation
The dataset was checked after scraping:
- Records collected: 20
- Missing values: 0
- Duplicate rows: 0

## Disclaimer
This project uses Books to Scrape, a practice website intended for learning web scraping. It is an educational project created for the CodeAlpha Python Development internship.
