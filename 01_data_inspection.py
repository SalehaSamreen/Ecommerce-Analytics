import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv", encoding="latin1")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate Order IDs:")
print(df["Order ID"].duplicated().sum())

print("\nUnique values:")
print(df.nunique())

print("\nNumeric summary:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())

print("\nDate range:")
print("Order Date:", df["Order Date"].min(), "to", df["Order Date"].max())
print("Ship Date:", df["Ship Date"].min(), "to", df["Ship Date"].max())

print("\nOrders where Ship Date is before Order Date:")
print((pd.to_datetime(df["Ship Date"]) < pd.to_datetime(df["Order Date"])).sum())