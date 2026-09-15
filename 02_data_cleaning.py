import pandas as pd

# Load raw dataset
df = pd.read_csv(
    "data/ecommerce_sales.csv",
    encoding="latin1"
)

print("Original shape:", df.shape)

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Remove leading/trailing spaces from Product Name
df["Product Name"] = df["Product Name"].str.strip()

# Save cleaned dataset
df.to_csv(
    "data/processed/ecommerce_sales_cleaned.csv",
    index=False
)

print("Cleaned shape:", df.shape)
print("Cleaned dataset saved successfully.")

# Verify Product Name cleaning
print("\nPost-cleaning verification:")
print(
    "Product Names with extra spaces:",
    (df["Product Name"] != df["Product Name"].str.strip()).sum()
)