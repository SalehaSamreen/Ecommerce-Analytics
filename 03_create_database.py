import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv(
    "data/processed/ecommerce_sales_cleaned.csv"
)

print("Dataset loaded:", df.shape)

# Connect to SQLite database
connection = sqlite3.connect("data/ecommerce_analytics.db")

# Create table from the cleaned dataset
df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

# Close connection
connection.close()

print("SQLite database created successfully.")
print("Table created: sales")