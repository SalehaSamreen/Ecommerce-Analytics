# E-Commerce Sales & Profit Analytics

An end-to-end data analytics project analyzing e-commerce sales, profitability, customers, products, regions, and discount patterns using Python, SQL, and Power BI.

## 📌 Project Overview

The goal of this project is to understand:

- How overall sales and profit are performing
- Which categories and regions generate the most profit
- Which products generate high revenue but low or negative profit
- How discount levels are associated with profitability
- Which customers generate significant revenue and whether they are profitable
- Which areas require further business investigation

The project follows a practical analytics workflow:

**Raw Data → Data Cleaning → Python Analysis → SQL Analysis → Power BI Dashboard → Business Insights**

---

## 📊 Dataset

**Dataset:** Superstore Sales Dataset  
**Records:** 9,994  
**Time Period:** 2014–2017  
**Orders:** 5,009  
**Unique Customers:** 793  

The dataset contains information about:

- Orders
- Customers
- Products
- Categories and sub-categories
- Sales
- Quantity
- Discounts
- Profit
- Regions
- Order and shipping dates

---

## 🛠️ Tools & Technologies

- **Python**
  - Pandas
  - Data cleaning
  - Business analysis
- **SQL**
  - SQLite
  - Aggregations
  - Grouping
  - Business metrics
- **Power BI**
  - Data visualization
  - KPI cards
  - Slicers
  - Sales and profit trends
  - Category and regional analysis
- **DAX**
  - Power BI measures
- **Git & GitHub**
  - Version control

---

## 🔄 Project Workflow

### 1. Data Inspection

The raw dataset was inspected for:

- Dataset dimensions
- Missing values
- Duplicate records
- Duplicate order IDs
- Data types
- Unique values
- Date ranges
- Negative profit records
- Text formatting issues

Negative profit records were retained because they represent genuine business losses and are important for profitability analysis.

---

### 2. Data Cleaning

The dataset was cleaned using Python and Pandas.

Cleaning steps included:

- Converting order and shipping dates into datetime format
- Removing unnecessary whitespace from product names
- Checking for missing values
- Checking for duplicate records
- Validating date relationships
- Saving the cleaned dataset separately

The cleaned dataset is stored in:

```text
data/processed/ecommerce_sales_cleaned.csv