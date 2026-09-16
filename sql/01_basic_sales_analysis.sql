-- 1. Total Sales
SELECT
    SUM(Sales) AS total_sales
FROM sales;


-- 2. Total Profit
SELECT
    SUM(Profit) AS total_profit
FROM sales;


-- 3. Total Orders
SELECT
    COUNT(DISTINCT "Order ID") AS total_orders
FROM sales;


-- 4. Total Customers
SELECT
    COUNT(DISTINCT "Customer ID") AS total_customers
FROM sales;

-- Monthly Sales and Profit Analysis

SELECT
    strftime('%Y-%m', "Order Date") AS month,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY month
ORDER BY month;