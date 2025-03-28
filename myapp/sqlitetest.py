import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('test.db')  # Replace 'test.db' with your actual DB file name
cursor = conn.cursor()

# Example: Check all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Example: Select all data from a specific table (e.g., users)
cursor.execute("SELECT * FROM users;")  # Replace 'users' with your table name
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
