import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("data/ecommerce_analytics.db")

cursor = connection.cursor()

print("=== E-COMMERCE SALES ANALYSIS ===")

# 1. Total Sales
cursor.execute("""
    SELECT
        SUM(Sales) AS total_sales
    FROM sales
""")

total_sales = cursor.fetchone()[0]

print("\n1. Total Sales:")
print(f"{total_sales:,.2f}")


# 2. Total Profit
cursor.execute("""
    SELECT
        SUM(Profit) AS total_profit
    FROM sales
""")

total_profit = cursor.fetchone()[0]

print("\n2. Total Profit:")
print(f"{total_profit:,.2f}")


# 3. Total Orders
cursor.execute("""
    SELECT
        COUNT(DISTINCT "Order ID") AS total_orders
    FROM sales
""")

total_orders = cursor.fetchone()[0]

print("\n3. Total Orders:")
print(total_orders)


# 4. Total Customers
cursor.execute("""
    SELECT
        COUNT(DISTINCT "Customer ID") AS total_customers
    FROM sales
""")

total_customers = cursor.fetchone()[0]

print("\n4. Total Customers:")
print(total_customers)

# 5. Monthly Sales and Profit
cursor.execute("""
    SELECT
        strftime('%Y-%m', "Order Date") AS month,
        ROUND(SUM(Sales), 2) AS total_sales,
        ROUND(SUM(Profit), 2) AS total_profit
    FROM sales
    GROUP BY month
    ORDER BY month
""")

monthly_results = cursor.fetchall()

print("\n5. Monthly Sales and Profit:")
print("Month       Sales          Profit")

for month, sales, profit in monthly_results:
    print(f"{month}   {sales:,.2f}      {profit:,.2f}")


# Close database connection
connection.close()

print("\nAnalysis completed successfully.")