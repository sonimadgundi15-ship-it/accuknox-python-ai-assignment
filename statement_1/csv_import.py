import csv
import sqlite3

csv_filename = "users_data.csv"
database_filename = "users.db"

print("Starting the import process...")

connection = sqlite3.connect(database_filename)
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
"""
)
print("Database table is ready.")

with open(csv_filename, mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)

    counter = 0
    for row in csv_reader:
        user_name = row["name"]
        user_email = row["email"]

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user_name, user_email),
        )
        counter = counter + 1
        print(f"Added: {user_name} ({user_email})")

connection.commit()
connection.close()

print("--------------------------------------------------")
print(f"Success! Finished importing {counter} users to the database.")

# CSv file -> read data using python -> insert data into db -> retrive data -> print data