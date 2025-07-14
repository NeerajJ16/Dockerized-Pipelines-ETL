import os
import requests
import psycopg2
from dotenv import load_dotenv

# Load .env file for database credentials
load_dotenv()

# Connect to PostgreSQL using credentials from .env
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        name TEXT
    );
""")

# Fetch data from public API
print("🔄 Fetching data from API...")
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

# Insert into PostgreSQL
for user in users:
    cur.execute(
        "INSERT INTO users (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;",
        (user['id'], user['name'])
    )

conn.commit()
cur.close()
conn.close()
print("✅ Data loaded into Railway PostgreSQL.")
