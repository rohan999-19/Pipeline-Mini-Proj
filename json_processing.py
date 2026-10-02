import json

# Load users.json
with open("users.json", "r") as file:
    users = json.load(file)

# Load books.json
with open("books.json", "r") as file:
    books = json.load(file)


# C1 - Total records
print("Total Users:", len(users))
print("Total Books:", len(books))


# C2 - Books with rating greater than 4
print("\nBooks With Rating Greater Than 4")
print("-" * 50)

for book in books:

    if book["rating"] > 4:
        print(book["title"], "-", book["rating"])


# C3 - Users whose company contains Group
print("\nUsers Whose Company Contains 'Group'")
print("-" * 50)

for user in users:

    if "Group" in user["company"]:
        print(user["name"], "-", user["company"])


# Average price
total_price = 0

for book in books:
    total_price += book["price"]

average_price = total_price / len(books)


# C4 - Combined report
report = {
    "total_users": len(users),
    "total_books": len(books),
    "average_price": round(average_price, 2)
}


# Save report
with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nreport.json created successfully.")
print(report)