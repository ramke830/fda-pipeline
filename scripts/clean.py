import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/fda_events.csv")
print("Before cleaning:", len(df), "rows")

df = df.dropna(subset=["drug_name", "reaction"])
df["drug_name"] = df["drug_name"].str.upper().str.strip()
df["reaction"] = df["reaction"].str.strip()
df["country"] = df["country"].fillna("Unknown")
df["serious"] = df["serious"].map({1: "Serious", 2: "Not Serious"}).fillna("Unknown")
df = df.drop_duplicates()

print("After cleaning:", len(df), "rows")
df.to_csv("data/processed/fda_clean.csv", index=False)
print("Saved!")
print(df.head())