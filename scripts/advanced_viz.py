import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings('ignore')

# Connect using SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:admin123@127.0.0.1/fda_db')
df = pd.read_sql('SELECT * FROM drug_events', engine)
print(f"Loaded {len(df)} records")

sns.set_theme(style="whitegrid", palette="muted")

# ── Chart 1: Heatmap — Drug vs Serious ──────────────────────────────
print("Generating heatmap...")
top_drugs = df['drug_name'].value_counts().head(10).index
df_top = df[df['drug_name'].isin(top_drugs)]
pivot = pd.crosstab(df_top['drug_name'], df_top['serious'])

plt.figure(figsize=(10, 7))
sns.heatmap(pivot, annot=True, fmt='d', cmap='Blues',
            linewidths=0.5, linecolor='gray',
            cbar_kws={'label': 'Number of Reports'})
plt.title('Heatmap: Top 10 Drugs vs Event Severity', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Severity', fontsize=11)
plt.ylabel('Drug Name', fontsize=11)
plt.tight_layout()
plt.savefig('data/processed/heatmap_drug_severity.png', dpi=150)
plt.show()
print("Heatmap saved!")

# ── Chart 2: Stacked Bar — Serious vs Not Serious per Drug ──────────
print("Generating stacked bar...")
pivot_pct = pivot.div(pivot.sum(axis=1), axis=0) * 100

pivot_pct.plot(kind='barh', stacked=True, figsize=(11, 6),
               color=['#E74C3C', '#3498DB'])
plt.title('Serious vs Not Serious Events per Drug (%)',
          fontsize=14, fontweight='bold')
plt.xlabel('Percentage (%)')
plt.ylabel('Drug Name')
plt.legend(title='Severity', loc='lower right')
plt.tight_layout()
plt.savefig('data/processed/stacked_bar_severity.png', dpi=150)
plt.show()
print("Stacked bar saved!")

# ── Chart 3: Reaction Frequency Heatmap ─────────────────────────────
print("Generating reaction heatmap...")
top_reactions = df['reaction'].value_counts().head(8).index
top_drugs_10 = df['drug_name'].value_counts().head(8).index
df_sub = df[df['drug_name'].isin(top_drugs_10) & df['reaction'].isin(top_reactions)]
pivot2 = pd.crosstab(df_sub['reaction'], df_sub['drug_name'])

plt.figure(figsize=(13, 7))
sns.heatmap(pivot2, annot=True, fmt='d', cmap='YlOrRd',
            linewidths=0.5, linecolor='gray')
plt.title('Heatmap: Reactions vs Drugs (Top 8 Each)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Drug Name', fontsize=11)
plt.ylabel('Reaction', fontsize=11)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('data/processed/heatmap_reaction_drug.png', dpi=150)
plt.show()
print("Reaction heatmap saved!")

# ── Chart 4: Country Distribution ───────────────────────────────────
print("Generating country chart...")
country_counts = df[df['country'] != 'Unknown']['country'].value_counts().head(10)

plt.figure(figsize=(10, 5))
bars = plt.barh(country_counts.index[::-1], country_counts.values[::-1],
                color=sns.color_palette("viridis", len(country_counts)))
plt.title('Adverse Event Reports by Country (Top 10)',
          fontsize=14, fontweight='bold')
plt.xlabel('Number of Reports')
for bar, val in zip(bars, country_counts.values[::-1]):
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             str(val), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('data/processed/country_distribution.png', dpi=150)
plt.show()
print("Country chart saved!")

# ── Chart 5: Summary Dashboard ───────────────────────────────────────
print("Generating summary dashboard...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('FDA Drug Adverse Events — BI Dashboard\nRamakrishna Lavoori | MADSC301',
             fontsize=16, fontweight='bold', y=1.01)

# Top drugs
top10 = df['drug_name'].value_counts().head(10)
axes[0,0].barh(top10.index[::-1], top10.values[::-1], color='steelblue')
axes[0,0].set_title('Top 10 Reported Drugs', fontweight='bold')
axes[0,0].set_xlabel('Reports')

# Serious pie
serious = df['serious'].value_counts()
axes[0,1].pie(serious.values, labels=serious.index,
              autopct='%1.1f%%', colors=['#E74C3C','#3498DB'], startangle=90)
axes[0,1].set_title('Serious vs Not Serious', fontweight='bold')

# Top reactions
top_r = df['reaction'].value_counts().head(8)
axes[1,0].barh(top_r.index[::-1], top_r.values[::-1], color='mediumseagreen')
axes[1,0].set_title('Top 8 Reactions', fontweight='bold')
axes[1,0].set_xlabel('Count')

# Country
c = df[df['country']!='Unknown']['country'].value_counts().head(8)
axes[1,1].bar(c.index, c.values, color='mediumpurple')
axes[1,1].set_title('Reports by Country', fontweight='bold')
axes[1,1].set_xlabel('Country')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('data/processed/dashboard_summary.png', dpi=150, bbox_inches='tight')
plt.show()
print("Dashboard saved!")

print("\nAll charts saved to data/processed/")