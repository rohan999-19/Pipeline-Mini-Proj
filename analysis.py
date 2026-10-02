import json

# Load JSON files
with open("users.json", "r") as file:
    users = json.load(file)

with open("books.json", "r") as file:
    books = json.load(file)


# =====================================
# USER ANALYSIS
# =====================================

print("========== USER ANALYSIS ==========")

# Total Users
total_users = len(users)

print("Total Users:", total_users)


# Unique Companies
companies = []

for user in users:
    companies.append(user["company"])

unique_companies = set(companies)

print("Unique Companies:", len(unique_companies))

print("\nUnique Company Names:")

for company in unique_companies:
    print(company)


# Top 5 Companies Alphabetically
sorted_companies = sorted(unique_companies)

top_5_companies = sorted_companies[:5]

print("\nTop 5 Companies Alphabetically:")

for company in top_5_companies:
    print(company)


# =====================================
# BOOK ANALYSIS
# =====================================

print("\n========== BOOK ANALYSIS ==========")

# Average Price
total_price = 0

for book in books:
    total_price += book["price"]

average_price = total_price / len(books)

print("Average Price:", round(average_price, 2))


# Highest Rated Books
highest_rating = max(book["rating"] for book in books)

print("\nHighest Rating:", highest_rating)

print("Highest Rated Books:")

for book in books:

    if book["rating"] == highest_rating:
        print(book["title"])


# Number of books in each rating category
rating_count = {}

for book in books:

    rating = book["rating"]

    if rating not in rating_count:
        rating_count[rating] = 1
    else:
        rating_count[rating] += 1


print("\nBooks in Each Rating Category:")

for rating, count in sorted(rating_count.items()):
    print("Rating", rating, ":", count, "books")


# =====================================
# SUMMARY
# =====================================

print("\n========== SUMMARY ==========")

print("Total Users:", total_users)
print("Unique Companies:", len(unique_companies))
print("Total Books:", len(books))
print("Average Book Price:", round(average_price, 2))
print("Highest Rating:", highest_rating)