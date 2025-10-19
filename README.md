# Book Scraper

A simple web scraper that collects book information from [Books to Scrape](https://books.toscrape.com).  
It extracts data such as title, price, availability, rating, and product link, then saves everything into a CSV file.

This project was built as a learning exercise in web scraping using Python and BeautifulSoup.

---

## Features
- Scrapes multiple pages of the website.
- Extracts detailed book information.
- Saves results automatically into a `books.csv` file.
- Includes polite scraping delay to avoid overloading the website.

---

## Technologies Used
- **Python 3**
- **requests**
- **BeautifulSoup (bs4)**
- **pandas**
- **time (sleep)**

---

## Project Structure
├── scraper.py # Main scraper script
├── books.csv # Generated output file
└── README.md # Project description
