# chewie-scraper

Simple web scraping project built with Python to extract structured data from a real website.

## Overview

TThis project demonstrates how to collect and structure data from a real-world application using HTTP requests and HTML parsing.

The scraper extracts product names and prices from a live menu page and exports the data into a structured JSON format.

## Features

- HTTP data collection using `requests`
- HTML parsing with `BeautifulSoup`
- Extraction of product name and price
- Structured output in JSON format
- Basic error handling for missing elements

## Tech Stack

- Python
- requests
- BeautifulSoup

## What I Learned

- How to perform HTTP requests using Python
- How to parse and navigate HTML with BeautifulSoup
- Handling missing or inconsistent data during extraction
- Structuring scraped data into JSON format
- Basic error handling in data collection workflows

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/luccatrevisan/chewie-scraper.git
cd chewie-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the scraper:
```bash
python scraper.py
```

## Example Output
```json
[
  {
    "name": "Cookie Brigadeiro",
    "price": "R$11.00"
  }
]
```

## Disclaimer

All data is collected from a publicly accessible page that I built myself.

## Possible Improvements
- Add retry logic for failed requests
- Store data in a database (PostgreSQL)
- Expose data through a REST API (Django REST Framework)
- Add CLI arguments (e.g., limit number of items)

## ✉️ Contact

Lucca - [LinkedIn](https://www.linkedin.com/in/lucca-trevisan-86a181378/) | luccatrevisandev@gmail.com

---
**MIT License • Built with focus on learning and real-world problem solving**