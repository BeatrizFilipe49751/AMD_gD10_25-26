import pandas as pd
from ..utils import config

# Load CSV normally (don't convert '?' into NaN)
df = pd.read_csv(config.DATASETA1_PATH, na_filter=False)

# Remove last row "----..."
df = df.iloc[:-1]

# STEP 1 — Determine attribute types
types = []
for col in df.columns:
    # All attributes in the mushroom dataset are categorical
    types.append("discrete")

# STEP 2 — Detect class column by name
class_row = ["class"] + [""] * (len(df.columns) - 1)

# STEP 3 — Build .tab header
header = "\t".join(df.columns)
type_line = "\t".join(types)
class_line = "\t".join(class_row)

# STEP 4 — Convert data rows (no change to '?' values)
data = df.apply(lambda row: "\t".join(row.astype(str)), axis=1)

# STEP 5 — Save to .tab
with open(config.DATASETA1_ORANGE_PATH, "w", encoding="utf-8") as f:
    f.write(header + "\n")
    f.write(type_line + "\n")
    f.write(class_line + "\n")
    for row in data:
        f.write(row + "\n")

print("Conversion complete!")