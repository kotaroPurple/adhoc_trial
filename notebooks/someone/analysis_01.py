
# %%
from pathlib import Path

from data_processor.loader import load_sales_data

# %%
REPO_ROOT = Path('../../')

# %%
df = load_sales_data(REPO_ROOT / "data" / "processed" / "sales_data.csv")
print(df)
