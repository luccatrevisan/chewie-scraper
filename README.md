# chewie-scraper

Simple web scraping project built with Python to extract structured data from a real website.

## Overview

This project demonstrates how to collect and structure data from a web page using HTTP requests and HTML parsing.

The scraper accesses a public webpage, extracts product information, and exports the data into a structured JSON format.

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

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/legal-data-scraper.git
cd legal-data-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
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

This project is for educational purposes only.
All data collected comes from a page that I built in August 2025.

## Possible Improvements
- Add retry logic for failed requests
- Store data in a database (PostgreSQL)
- Expose data through a REST API (Django REST Framework)
- Add CLI arguments (e.g., limit number of items)