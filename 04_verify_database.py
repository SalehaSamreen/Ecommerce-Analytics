import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("data/ecommerce_analytics.db")

cursor = connection.cursor()

# Check row count
cursor.execute("SELECT COUNT(*) FROM sales")
row_count = cursor.fetchone()[0]

print("Rows in sales table:", row_count)

# Check columns
cursor.execute("PRAGMA table_info(sales)")
columns = cursor.fetchall()

print("\nColumns in sales table:")
for column in columns:
    print(column[1], "-", column[2])

# Close connection
connection.close()

print("\nDatabase verification completed successfully.")