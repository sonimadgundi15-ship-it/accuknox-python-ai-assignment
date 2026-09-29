import requests
import sqlite3


# print("Request is working")

url = "https://openlibrary.org/search.json?q=python"

response = requests.get(url)
data = response.json()
# print(data)

books = data['docs']

db_connection = sqlite3.connect("books.db")
# print("db connected")

cursor = db_connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
""")
cursor.execute

for i in books:
    authors = i.get("author_name") or []
    author = ", ".join(authors)
    publication_year = i.get('first_publish_year')
    title = i.get('title')

   
    cursor.execute("""
        INSERT INTO books(title, author, publication_year)
        VALUES (?, ?, ?) """,
        (title, author, publication_year)
    )

    db_connection.commit()

cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

for i in rows:
    print(i)


# Api - > Json data -> Exctracting book details -> store sqlite db -> Retrive data 