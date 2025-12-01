import pandas as pd
from ..utils import config

# Load the CSV file exactly as it is (keep '?' not converting to NaN)
df = pd.read_csv(config.DATASETA1_PATH)

# Remove the last row, which contains only "----" separators in the original dataset
df = df.iloc[:-1]

# STEP 1 — Orange requires a "type" line: all attributes here are discrete
types = ["discrete"] * len(df.columns)

# STEP 2 — Orange requires a "class" line: only the first column is the class label
class_row = ["class"] + [""] * (len(df.columns) - 1)

# STEP 3 — Build .tab header
header = "\t".join(df.columns)      # column names
type_line = "\t".join(types)        # attribute types
class_line = "\t".join(class_row)   # class marker

# STEP 4 — Convert each data row into tab-separated text
data = df.apply(lambda row: "\t".join(row.astype(str)), axis=1)

# STEP 5 — Write everything to the .tab file
with open(config.DATASETA1_ORANGE_PATH, "w", encoding="utf-8") as f:
    f.write(header + "\n")
    f.write(type_line + "\n")
    f.write(class_line + "\n")
    for row in data:
        f.write(row + "\n")

print("Conversion complete!")