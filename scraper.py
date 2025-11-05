import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

books_csv = []


def get_page(pages):
    for p in range(1, pages + 1):
        url = f"https://books.toscrape.com/catalogue/page-{p}.html"
        html = requests.get(url)

# Checking web status
        if html.status_code != 200:
            break

        soup = BeautifulSoup(html.text, "html.parser")
        books = soup.find_all("article", class_ = "product_pod")

        parse_book(books)

        print(f"Pages: {p}/{pages}")
    

# Saving everything to CSV
    save_to_csv()



def parse_book(books):
    global books_csv

# Searching for all info we need
    for book in books:
        title = book.find("h3").find("a").get("title")
        price = book.find("div", class_= "product_price").find("p", class_= "price_color").text
        link = "https://books.toscrape.com/catalogue/" + book.find("h3").find("a").get("href")
        html = requests.get(url = link)

        if html.status_code != 200:
            what = int(f"Catalogue page for book {title} is not working. Do you want to skip it and continue?\n1. Skip    |   2. Stop")
            if what == 1:
                pass
            elif what == 2:
                break
            else:
                return
# Searching for more info in book catalogue
        books_catalogue = BeautifulSoup(html.text, "html.parser")
        availability = books_catalogue.find("p", class_="instock availability").text.strip()
        rating_tag = books_catalogue.find("p", class_="star-rating")
        if rating_tag:
            classes = rating_tag.get("class")
            rating = [c for c in classes if c != "star-rating"][0]
        else:
            rating = None

# Puting info about book we just search together in books_csv
        books_csv.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "Link": link
        })

# Making sure that we won't put too much task on the web we are scraping
        sleep(1)

def save_to_csv():

# Puting it all to the csv file
    pd.DataFrame(books_csv).to_csv("books.csv", index=False)
    print("Saved...")

get_page(10)
