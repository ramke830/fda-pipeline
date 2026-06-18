# FDA Drug Adverse Events — BI Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

**Course:** MADSC301 — Business Intelligence  
**Student:** Ramakrishna Lavoori | **ID:** 25056894  
**Professor:** Dr. Zainab Usman | **Term:** 3 — AY 2025/26

---

## Business Case
Analyzing FDA adverse drug event reports to identify which drugs cause the most side effects — helping hospitals, pharmacies, and health regulators make safer decisions.

---

## Technology Stack

| Area | Technology |
|------|------------|
| Data source | OpenFDA API |
| Programming language | Python 3.11 |
| Data cleaning | Pandas and NumPy |
| Development environment | Jupyter Notebook + VS Code |
| Database | PostgreSQL 18 |
| Database administration | pgAdmin 4 |
| Database connection | psycopg2 + SQLAlchemy |
| Workflow orchestration | pipeline.py + Windows Task Scheduler |
| Data analysis | SQL, Pandas, Seaborn, Matplotlib |
| Version control | Git and GitHub |

---

## Pipeline Architecture


---

## Project Folder Structure

---

## Dashboard Results

| KPI | Result |
|-----|--------|
| Total records collected | 100 |
| Unique drugs | 89 |
| Unique reactions | 67 |
| Most reported drug | LETAIRIS (168 reports) |
| Most common reaction | Dyspnoea |
| Serious events | 34% |
| Not serious events | 66% |

---

## Screenshots

### Summary Dashboard
![Dashboard](screenshots/dashboard_summary.png)

### Heatmap — Drug vs Severity
![Heatmap](screenshots/heatmap_drug_severity.png)

### Heatmap — Reactions vs Drugs
![Reaction Heatmap](screenshots/heatmap_reaction_drug.png)

### Severity Breakdown per Drug
![Stacked Bar](screenshots/stacked_bar_severity.png)

---

## Key Insights

1. LETAIRIS dominates adverse event reports with 168 occurrences
2. 66% of reported events were classified as Not Serious
3. Dyspnoea (shortness of breath) is the most common reaction
4. Many reports lack country data — showing a global reporting gap
5. Common OTC drugs like Ibuprofen also appear in serious event reports
6. 100% of PREDNISONE, RANOLAZINE and BENLYSTA reports were Serious

---

## Recommendations

1. Health regulators should closely monitor LETAIRIS prescriptions
2. Dyspnoea as a top reaction warrants urgent clinical attention
3. Improve global reporting systems to capture country data
4. Schedule daily pipeline runs to track new adverse events
5. Expand dataset to 1000+ records for deeper trend analysis

---

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/ramke830/fda-pipeline.git
cd fda_pipeline
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create the .env file

### 5. Create PostgreSQL database
Open pgAdmin and run:

### 6. Run the full ETL pipeline
```bash
python pipeline.py
```

### 7. Run advanced visualizations
```bash
python scripts/advanced_viz.py
```

### 8. Run SQL analysis queries
```bash
python scripts/run_queries.py
```

### 9. Open Jupyter notebook
```bash
jupyter notebook notebooks/fda_analysis.ipynb
```

---

## How to Run the Pipeline

**Direct Python:**
```bash
python pipeline.py
```

**Windows batch file:**
```bash
scripts\run_pipeline.bat
```

---

## Security
- Credentials stored in `.env` file
- `.env` and `venv/` excluded via `.gitignore`
- PostgreSQL password not included in repository

---

## Limitations
1. Dataset limited to 100 records per API call
2. Some reports lack country information
3. Drug names may have spelling variations
4. API results may change between extraction times

---

## Future Improvements
- Collect 1000+ records for deeper analysis
- Add machine learning for reaction prediction
- Docker containerisation
- Email notifications for pipeline failures
- Historical trend tracking with daily scheduling

---

## Author
**Ramakrishna Lavoori**  
Business Intelligence Final Assignment — MADSC301  
EU Business School Munich — Spring Semester 2026  
GitHub: [ramke830](https://github.com/ramke830)