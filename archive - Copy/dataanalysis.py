import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Optional dependency: scikit-learn is only used for StandardScaler.
# If it's not installed, fall back to a NumPy implementation.
try:
    from sklearn.preprocessing import StandardScaler  # type: ignore
except ModuleNotFoundError:
    StandardScaler = None  # type: ignore

# 1. Load Data
# Using 'unicode_escape' to handle special characters often found in CSVs
script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, 'Diwali Sales Data.csv'), encoding='unicode_escape')

# --- DATA CLEANING ---

# 2. Identify and Handle Missing Values
# Goal: Identify nulls, ensure no column is filled more than 40%, 
# and ensure zero nulls remain at the end.
print("Initial Missing Values:\n", df.isnull().sum())

# Drop columns that are entirely empty (like 'Status' and 'unnamed1' in this dataset)
df.dropna(axis=1, how='all', inplace=True)

# Calculation: Fill nulls only if they represent < 40% of the column.
# If they represent more, we must drop the column or rows to ensure 0 nulls remain.
for col in df.columns:
    null_count = df[col].isnull().sum()
    null_ratio = null_count / len(df)
    
    if null_count > 0:
        if null_ratio <= 0.40:
            # Fill numeric with median, categorical with mode
            if df[col].dtype in ['int64', 'float64']:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
        else:
            # If > 40% is null, drop the column to satisfy the requirement
            df.drop(columns=[col], inplace=True)

# Final sweep to ensure no nulls remain (dropping remaining rows with nulls if any)
df.dropna(inplace=True)

# 3. Remove Duplicate Records
duplicate_count = df.duplicated().sum()
df.drop_duplicates(inplace=True)
print(f"Removed {duplicate_count} duplicate records.")

# --- STATISTICAL ANALYSIS ---

# 4. Detect Outliers using IQR Method
# We will focus on the 'Amount' column as it is the primary target for sales analysis
Q1 = df['Amount'].quantile(0.25)
Q3 = df['Amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Amount'] < lower_bound) | (df['Amount'] > upper_bound)]
print(f"Outliers detected in Amount: {len(outliers)}")

# --- FEATURE ENGINEERING ---

# 5. Feature Scaling (Standardization)
# We apply StandardScaler to 'Age', 'Orders', and 'Amount'
cols_to_scale = ['Age', 'Orders', 'Amount']
df_scaled = df.copy()
if StandardScaler is not None:
    scaler = StandardScaler()
    df_scaled[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    print("Feature scaling complete using scikit-learn StandardScaler.")
else:
    # NumPy fallback equivalent to StandardScaler (with population std, ddof=0).
    for col in cols_to_scale:
        mean = df[col].mean()
        std = df[col].std(ddof=0)
        if std == 0 or np.isnan(std):
            df_scaled[col] = 0.0
        else:
            df_scaled[col] = (df[col] - mean) / std
    print("Feature scaling complete using NumPy fallback (no scikit-learn).")

# --- VISUALIZATION ---

# 6. Correlation Matrix Heatmap
plt.figure(figsize=(10, 6))
# Only include numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# 7. Data Distribution Plots
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Plot A: Gender distribution by Amount (Total Sales)
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum()
sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=axes[0])
axes[0].set_title('Total Sales Amount by Gender')

# Plot B: Age Group Distribution
sns.countplot(data=df, x='Age Group', hue='Gender', ax=axes[1])
axes[1].set_title('Customer Count by Age Group & Gender')

plt.tight_layout()
plt.show()

print("Analysis Complete. Data is clean, scaled, and visualized.")