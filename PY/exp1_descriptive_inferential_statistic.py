# -*- coding: utf-8 -*-
"""Exp1_Descriptive_Inferential_Statistic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fd7NfAO1021OF746KIL3hHlXGo7-2lAA
"""

# ✅ STEP 1: Import necessary libraries
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ✅ STEP 2: Load dataset
df = sns.load_dataset("iris")
df.head()

# ✅ Basic descriptive statistics
print("Descriptive Statistics:\n")
print(df.describe())

# ✅ Additional insights on numeric data only
numeric_df = df.select_dtypes(include=[np.number])
print("\nMedian of each numeric column:\n", numeric_df.median())
print("\nMode of each column:\n", df.mode().iloc[0])
print("\nStandard Deviation:\n", numeric_df.std())

# ✅ Create subsets
setosa = df[df['species'] == 'setosa']['petal_length']
virginica = df[df['species'] == 'virginica']['petal_length']

# ✅ T-Test
t_stat, p_val = stats.ttest_ind(setosa, virginica)
print(f"\nT-Test between Setosa and Virginica Petal Lengths:")
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_val:.4f}")

# ✅ Interpretation
if p_val < 0.05:
    print("✅ Significant difference found between Setosa and Virginica petal lengths.")
else:
    print("❌ No significant difference found.")

# ✅ Correlation
correlation = df['sepal_length'].corr(df['petal_length'])
print(f"\nCorrelation between Sepal Length and Petal Length: {correlation:.4f}")