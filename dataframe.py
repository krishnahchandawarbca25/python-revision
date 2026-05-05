import pandas as pd
from pathlib import Path

data = {"name": ["John", "Jane", "Jim", "Jill"], "age": [25, 30, 35, 40], "city": ["New York", "Los Angeles", "Chicago", "Houston"]}

df_scratch = pd.DataFrame(data)
print(df_scratch)

csv_path = Path("dataset.csv")
if not csv_path.exists():
    csv_path = Path("archive - Copy") / "dataset.csv"

df = pd.read_csv(csv_path)
print(df)
df.drop_duplicates(inplace=True)
print(df)
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)

