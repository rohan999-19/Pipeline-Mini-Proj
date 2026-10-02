import requests
import json

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data from API
response = requests.get(url)

# Check status
print("API Status Code:", response.status_code)

# Convert JSON response into Python object
users = response.json()

# Processed user data
processed_users = []

for user in users:

    user_data = {
        "name": user["name"],
        "email": user["email"],
        "company": user["company"]["name"]
    }

    processed_users.append(user_data)

# A1 - Display user information
print("\nUSER DATA")
print("-" * 40)

for user in processed_users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Company:", user["company"])
    print()

# A2 - Total users
print("Total Users:", len(processed_users))

# A3 - Extract company names
company_names = []

for user in processed_users:
    company_names.append(user["company"])

print("\nCompany Names:")
for company in company_names:
    print(company)

# A5 - Save processed data into users.json
with open("users.json", "w") as file:
    json.dump(processed_users, file, indent=4)

print("\nusers.json created successfully.")
