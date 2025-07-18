import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Prefer v2 results if available
CSV_PATH = ROOT / "analysis" / "full_results_v2.csv"
if not CSV_PATH.exists():
    CSV_PATH = ROOT / "analysis" / "full_results.csv"
OUT_DIR = Path(__file__).parent
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Load and filter
pdf = pd.read_csv(CSV_PATH)
loc = pdf[pdf['is_locatable'].astype(str).isin(['1', 'True', 'true'])].copy()
loc['error_km'] = pd.to_numeric(loc['error_km'], errors='coerce')
loc = loc.dropna(subset=['error_km'])

# Define custom order: Ensemble (E), M-series, T-series, then H-series baselines
method_order = ['E-1', 'E-2',
               'M-1', 'M-2', 'M-3', 'M-4', 'M-5', 'M-6',
               'T-1', 'T-4',
               'H-1', 'H-2', 'H-3', 'H-4']
# Filter to only include methods that exist in our data
method_order = [m for m in method_order if m in loc['method_id'].unique()]

counts = loc['method_id'].value_counts()
keep_methods = counts[counts >= 20].index.tolist()
for baseline in ['H-3', 'H-4']:
    if baseline in loc['method_id'].unique() and baseline not in keep_methods:
        keep_methods.append(baseline)

# apply filter now that list is final
loc = loc[loc['method_id'].isin(keep_methods)]

plt.figure(figsize=(10, 6))
sns.violinplot(data=loc, x='method_id', y='error_km', inner='quartile', palette='muted', cut=0, order=method_order)
plt.ylabel('Error (km)')
plt.xlabel('Method')
plt.title('Error distribution per method')
plt.tight_layout()
plt.savefig(OUT_DIR / 'error_violin_methods.png', dpi=300)
plt.savefig(OUT_DIR / 'error_violin_methods.pdf')
print('Violin plot saved.') 