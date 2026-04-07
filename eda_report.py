"""
Reusable EDA Report Generator
Works on any pandas DataFrame
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_eda_report(
    df,
    output_dir="output_auto",
    numeric_only=True,
    plot_style="whitegrid"
):
    """
    Generate a full EDA report for any dataset.

    Args:
        df: pandas DataFrame
        output_dir: where outputs will be saved
        numeric_only: whether to focus on numeric columns
        plot_style: seaborn style
    """

    os.makedirs(output_dir, exist_ok=True)
    sns.set_style(plot_style)

    # -------------------------
    # 1. Data Profile
    # -------------------------
    with open(f"{output_dir}/profile.txt", "w", encoding="utf-8") as f:
        f.write(f"Shape: {df.shape}\n\n")
        f.write("Data Types:\n")
        f.write(str(df.dtypes) + "\n\n")

        f.write("Missing Values:\n")
        f.write(str(df.isnull().sum()) + "\n\n")

        f.write("Missing %:\n")
        f.write(str((df.isnull().mean() * 100)) + "\n\n")

        f.write("Descriptive Stats:\n")
        f.write(str(df.describe()) + "\n")

    # -------------------------
    # 2. Select Columns
    # -------------------------
    if numeric_only:
        cols = df.select_dtypes(include="number").columns
    else:
        cols = df.columns

    # -------------------------
    # 3. Distribution Plots
    # -------------------------
    for col in cols:
        try:
            sns.histplot(df[col], kde=True)
            plt.title(f"{col} Distribution")
            plt.savefig(f"{output_dir}/{col}_distribution.png")
            plt.clf()
        except:
            pass  # skip problematic columns

    # -------------------------
    # 4. Correlation Heatmap
    # -------------------------
    numeric_cols = df.select_dtypes(include="number")

    if len(numeric_cols.columns) > 1:
        corr = numeric_cols.corr()

        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.savefig(f"{output_dir}/correlation_heatmap.png")
        plt.clf()

    # -------------------------
    # 5. Missing Data Visualization
    # -------------------------
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Data Heatmap")
    plt.savefig(f"{output_dir}/missing_data.png")
    plt.clf()

    # -------------------------
    # 6. Outlier Detection (IQR)
    # -------------------------
    outliers = {}

    for col in numeric_cols.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        count = df[(df[col] < lower) | (df[col] > upper)].shape[0]
        outliers[col] = count

    with open(f"{output_dir}/outliers.txt", "w") as f:
        for k, v in outliers.items():
            f.write(f"{k}: {v} outliers\n")

    print(f"\nEDA report generated in: {output_dir}")