import pandas as pd


# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

df = pd.read_csv(
    "data/processed/ecommerce_sales_cleaned.csv"
)

print("Dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 2. OVERALL BUSINESS PERFORMANCE
# ============================================================

total_revenue = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
profit_margin = (total_profit / total_revenue) * 100

print("\nOverall Business Performance")
print("-" * 35)
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Unique Customers: {total_customers:,}")
print(f"Profit Margin: {profit_margin:.2f}%")


# ============================================================
# 3. MONTHLY REVENUE & PROFIT ANALYSIS
# ============================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly = (
    df.groupby(df["Order Date"].dt.to_period("M"))
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum")
      )
      .reset_index()
)

monthly["Order Date"] = monthly["Order Date"].astype(str)

print("\nMonthly Revenue & Profit")
print("-" * 35)
print(monthly.to_string(index=False))


# ============================================================
# 4. CATEGORY PERFORMANCE
# ============================================================

category_analysis = (
    df.groupby("Category")
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .reset_index()
)

category_analysis["Profit Margin %"] = (
    category_analysis["Profit"] /
    category_analysis["Revenue"] * 100
)

category_analysis = category_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\nCategory Performance")
print("-" * 35)
print(category_analysis.to_string(index=False))


# ============================================================
# 5. DISCOUNT VS PROFITABILITY
# ============================================================

discount_analysis = (
    df.groupby("Discount")
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order ID", "nunique")
      )
      .reset_index()
)

discount_analysis["Profit Margin %"] = (
    discount_analysis["Profit"] /
    discount_analysis["Revenue"] * 100
)

print("\nDiscount vs Profitability")
print("-" * 35)
print(discount_analysis.to_string(index=False))


# ============================================================
# 6. REGION PERFORMANCE
# ============================================================

region_analysis = (
    df.groupby("Region")
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order ID", "nunique")
      )
      .reset_index()
)

region_analysis["Profit Margin %"] = (
    region_analysis["Profit"] /
    region_analysis["Revenue"] * 100
)

region_analysis = region_analysis.sort_values(
    "Profit",
    ascending=False
)

print("\nRegional Performance")
print("-" * 35)
print(region_analysis.to_string(index=False))


# ============================================================
# 7. TOP 10 PRODUCTS BY REVENUE
# ============================================================

top_products = (
    df.groupby(["Product ID", "Product Name"])
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum")
      )
      .reset_index()
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print("\nTop 10 Products by Revenue")
print("-" * 35)
print(top_products.to_string(index=False))


# ============================================================
# 8. TOP 10 CUSTOMERS BY REVENUE
# ============================================================

top_customers = (
    df.groupby(["Customer ID", "Customer Name"])
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order ID", "nunique")
      )
      .reset_index()
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print("\nTop 10 Customers by Revenue")
print("-" * 35)
print(top_customers.to_string(index=False))


# ============================================================
# 9. LOSS-MAKING PRODUCTS
# ============================================================

loss_products = (
    df.groupby(["Product ID", "Product Name"])
      .agg(
          Revenue=("Sales", "sum"),
          Profit=("Profit", "sum")
      )
      .reset_index()
)

loss_products = (
    loss_products[loss_products["Profit"] < 0]
    .sort_values("Profit")
    .head(10)
)

print("\nTop 10 Loss-Making Products")
print("-" * 35)
print(loss_products.to_string(index=False))


# ============================================================
# 10. BUSINESS INSIGHTS
# ============================================================

best_revenue_month = monthly.loc[
    monthly["Revenue"].idxmax()
]

best_profit_month = monthly.loc[
    monthly["Profit"].idxmax()
]

loss_months = monthly[
    monthly["Profit"] < 0
]

best_category = category_analysis.iloc[0]

lowest_margin_category = category_analysis.loc[
    category_analysis["Profit Margin %"].idxmin()
]

best_region = region_analysis.iloc[0]


print("\nKey Business Insights")
print("-" * 35)

print(
    f"Highest revenue month: "
    f"{best_revenue_month['Order Date']} "
    f"(${best_revenue_month['Revenue']:,.2f})"
)

print(
    f"Highest profit month: "
    f"{best_profit_month['Order Date']} "
    f"(${best_profit_month['Profit']:,.2f})"
)

print(
    f"Number of loss-making months: "
    f"{len(loss_months)}"
)

print(
    f"Most profitable category: "
    f"{best_category['Category']} "
    f"(${best_category['Profit']:,.2f})"
)

print(
    f"Lowest-margin category: "
    f"{lowest_margin_category['Category']} "
    f"({lowest_margin_category['Profit Margin %']:.2f}%)"
)

print(
    f"Most profitable region: "
    f"{best_region['Region']} "
    f"(${best_region['Profit']:,.2f})"
)

print("\nAnalysis completed successfully.")