import requests
from bs4 import BeautifulSoup
import json

# Website URL
url = "https://books.toscrape.com"

# Fetch webpage
response = requests.get(url)

print("Website Status Code:", response.status_code)

response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

books = []

book_items = soup.find_all("article", class_="product_pod")

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

for book in book_items[:20]:

    title = book.h3.a["title"]

    price_text = book.find(
        "p",
        class_="price_color"
    ).text.strip()

    price = float(
        price_text.replace("£", "").replace("Â", "")
    )

    rating_text = book.find(
        "p",
        class_="star-rating"
    )["class"][1]

    rating = rating_map[rating_text]

    book_data = {
        "title": title,
        "price": price,
        "rating": rating
    }

    books.append(book_data)


# B1/B2 - Display books
print("\nBOOK DATA")
print("-" * 60)

for book in books:
    print("Title:", book["title"])
    print("Price:", book["price"])
    print("Rating:", book["rating"])
    print()


# B4 - Most expensive book
most_expensive = max(books, key=lambda x: x["price"])

# B4 - Least expensive book
least_expensive = min(books, key=lambda x: x["price"])

# B4 - Average price
total_price = 0

for book in books:
    total_price += book["price"]

average_price = total_price / len(books)

print("Most Expensive Book:")
print(most_expensive)

print("\nLeast Expensive Book:")
print(least_expensive)

print("\nAverage Book Price:", round(average_price, 2))


# B5 - Save data
with open("books.json", "w") as file:
    json.dump(books, file, indent=4)

print("\nbooks.json created successfully.")