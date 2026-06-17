import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    database="fda_db",
    user="postgres",
    password="admin123"  # empty because we set trust authentication
)

cursor = conn.cursor()

# Load cleaned data
df = pd.read_csv("data/processed/fda_clean.csv")
print(f"Loading {len(df)} rows into PostgreSQL...")

# Prepare rows
rows = [
    (
        row["report_id"],
        row["country"],
        row["serious"],
        row["drug_name"],
        row["reaction"]
    )
    for _, row in df.iterrows()
]

# Insert into database
execute_values(cursor, """
    INSERT INTO drug_events (report_id, country, serious, drug_name, reaction)
    VALUES %s
""", rows)

conn.commit()
cursor.close()
conn.close()

print("Done! Data loaded into PostgreSQL ✅")