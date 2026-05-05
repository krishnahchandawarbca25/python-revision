import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

csv_path = Path("Diwali Sales Data.csv")
if not csv_path.exists():
    csv_path = Path("archive - Copy") / "Diwali Sales Data.csv"

df = pd.read_csv(csv_path, encoding="unicode_escape")
df.info()
df.head() 
numeric_df = df.select_dtypes(include=[np.number])
numeric_df.min()
numeric_df.max()
numeric_df.var()
numeric_df.std()
numeric_df.describe()
numeric_df.quantile()
numeric_df.median()
df.mode()
numeric_df.skew()
numeric_df.kurt()
df["Product_Category"].value_counts()