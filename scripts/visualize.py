import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect and load data
conn = psycopg2.connect(
    host="127.0.0.1",
    database="fda_db",
    user="postgres",
    password="admin123"
)

df = pd.read_sql("SELECT * FROM drug_events", conn)
conn.close()

# Chart 1 - Top 10 drugs with most reports
plt.figure(figsize=(12, 5))
df["drug_name"].value_counts().head(10).plot(kind="bar", color="steelblue")
plt.title("Top 10 Most Reported Drugs")
plt.xlabel("Drug Name")
plt.ylabel("Number of Reports")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("data/processed/top_drugs.png")
plt.show()

# Chart 2 - Serious vs Not Serious
plt.figure(figsize=(6, 5))
df["serious"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["tomato", "skyblue"])
plt.title("Serious vs Not Serious Events")
plt.ylabel("")
plt.tight_layout()
plt.savefig("data/processed/serious_pie.png")
plt.show()

# Chart 3 - Top 10 reactions
plt.figure(figsize=(12, 5))
df["reaction"].value_counts().head(10).plot(kind="bar", color="mediumseagreen")
plt.title("Top 10 Most Common Reactions")
plt.xlabel("Reaction")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("data/processed/top_reactions.png")
plt.show()

print("All charts saved to data/processed/ ✅")