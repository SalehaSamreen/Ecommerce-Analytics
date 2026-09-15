import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv", encoding="latin1")

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

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
print((df["Ship Date"] < df["Order Date"]).sum())

print("\nCategorical values:")

categorical_columns = [
    "Ship Mode",
    "Segment",
    "Country",
    "Region",
    "Category",
    "Sub-Category"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].unique())

print("\nInvalid numerical values:")

print("Sales <= 0:", (df["Sales"] <= 0).sum())
print("Quantity <= 0:", (df["Quantity"] <= 0).sum())
print("Discount < 0:", (df["Discount"] < 0).sum())
print("Discount > 1:", (df["Discount"] > 1).sum())

print("\nNegative profit rows:")
print((df["Profit"] < 0).sum())

print("\nText cleanliness check:")

text_columns = [
    "Order ID",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name"
]

for column in text_columns:
    leading_trailing_spaces = (df[column] != df[column].str.strip()).sum()
    print(f"{column}: {leading_trailing_spaces} values with extra spaces")

print("\nDate logic checks:")

print("Order Date missing:", df["Order Date"].isna().sum())
print("Ship Date missing:", df["Ship Date"].isna().sum())

print("Ship Date before Order Date:", (df["Ship Date"] < df["Order Date"]).sum())

print("Orders shipped more than 30 days after order:",
      (df["Ship Date"] - df["Order Date"]).dt.days.gt(30).sum())