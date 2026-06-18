from sqlalchemy import create_engine, text
import pandas as pd
import os

os.makedirs('reports', exist_ok=True)

engine = create_engine('postgresql+psycopg2://postgres:admin123@127.0.0.1/fda_db')

queries = {
    "1_summary_kpis": """
        SELECT COUNT(*) AS total_reports,
        COUNT(DISTINCT drug_name) AS unique_drugs,
        COUNT(DISTINCT reaction) AS unique_reactions,
        SUM(CASE WHEN serious='Serious' THEN 1 ELSE 0 END) AS serious_count,
        ROUND(SUM(CASE WHEN serious='Serious' THEN 1 ELSE 0 END)*100.0/COUNT(*),2)
        AS serious_pct
        FROM drug_events
    """,
    "2_top_drugs": """
        SELECT drug_name, COUNT(*) AS total_reports,
        RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
        FROM drug_events GROUP BY drug_name
        ORDER BY total_reports DESC LIMIT 10
    """,
    "3_top_reactions": """
        SELECT reaction, COUNT(*) AS total_count,
        ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(),2) AS percentage
        FROM drug_events GROUP BY reaction
        ORDER BY total_count DESC LIMIT 10
    """,
    "4_by_country": """
        SELECT country, COUNT(*) AS total,
        SUM(CASE WHEN serious='Serious' THEN 1 ELSE 0 END) AS serious,
        ROUND(SUM(CASE WHEN serious='Serious' THEN 1 ELSE 0 END)*100.0/COUNT(*),1)
        AS serious_pct
        FROM drug_events WHERE country != 'Unknown'
        GROUP BY country ORDER BY total DESC LIMIT 10
    """,
    "5_most_dangerous": """
        SELECT drug_name, COUNT(*) AS total_reports,
        ROUND(SUM(CASE WHEN serious='Serious' THEN 1 ELSE 0 END)*100.0/COUNT(*),1)
        AS serious_pct
        FROM drug_events GROUP BY drug_name
        HAVING COUNT(*) >= 3
        ORDER BY serious_pct DESC LIMIT 10
    """
}

print("Running professional SQL queries...\n")
with engine.connect() as conn:
    for name, query in queries.items():
        df = pd.read_sql(text(query), conn)
        print(f"=== {name.upper()} ===")
        print(df.to_string(index=False))
        print()
        df.to_csv(f"reports/{name}.csv", index=False)

print("All results saved to reports/ folder!")