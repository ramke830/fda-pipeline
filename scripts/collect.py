import requests
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

print("Fetching data from OpenFDA...")

# Call the FDA API - get 100 adverse drug event reports
url = "https://api.fda.gov/drug/event.json"
params = {
    "limit": 100
}

response = requests.get(url, params=params)
data = response.json()

# Pull out the results
results = data["results"]

# Extract only the columns we need
rows = []
for report in results:
    try:
        row = {
            "report_id": report.get("safetyreportid", ""),
            "country": report.get("occurcountry", ""),
            "serious": report.get("serious", ""),
            "drug_name": report["patient"]["drug"][0]["medicinalproduct"],
            "reaction": report["patient"]["reaction"][0]["reactionmeddrapt"]
        }
        rows.append(row)
    except:
        pass  # skip incomplete records

# Save to CSV
df = pd.DataFrame(rows)
df.to_csv("data/raw/fda_events.csv", index=False)

print(f"Done! Collected {len(df)} records.")
print(df.head())