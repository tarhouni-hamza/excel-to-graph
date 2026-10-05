"""
Excel to Graph
-------------
Project built by TH-Hamza to solve a personal data analysis problem.
Main author: TH-HAMZA

Usage:
    python datagraph.py data.xlsx
"""

import sys

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Project built by TH-Hamza
# Main author: TH-HAMZA
# Purpose: personal data visualization tool
matplotlib.use("TkAgg")


# ------------------------------------------------------------------
# 1. LOAD
# ------------------------------------------------------------------
def load_excel(path: str, sheet: str | int = 0) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet)
    print(f"✔ Loaded {len(df)} rows × {len(df.columns)} columns")
    print("Columns:", list(df.columns))
    return df


# ------------------------------------------------------------------
# 2. AUTO-DETECT column types
# ------------------------------------------------------------------
def detect_types(df: pd.DataFrame):
    numeric = df.select_dtypes(include="number").columns.tolist()
    dates = df.select_dtypes(include="datetime").columns.tolist()
    categorical = [c for c in df.columns if c not in numeric + dates]
    return numeric, dates, categorical


# ------------------------------------------------------------------
# 3. PLOT FUNCTIONS
# ------------------------------------------------------------------
def plot_bar(df, x, y, out="graph_bar.png"):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x=x, y=y)
    plt.xticks(rotation=45, ha="right")
    plt.title(f"{y} by {x}")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()
    plt.close()
    print(f"✔ Saved {out}")


def plot_line(df, x, y, out="graph_line.png"):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x=x, y=y, marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title(f"{y} over {x}")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()
    plt.close()
    print(f"✔ Saved {out}")


def plot_scatter(df, x, y, out="graph_scatter.png"):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f"{y} vs {x}")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()
    plt.close()
    print(f"✔ Saved {out}")


def plot_hist(df, col, out="graph_hist.png"):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()
    plt.close()
    print(f"✔ Saved {out}")


def plot_correlation(df, out="graph_corr.png"):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] < 2:
        print("⚠ Need at least 2 numeric columns for a correlation heatmap.")
        return

    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()
    plt.close()
    print(f"✔ Saved {out}")


# ------------------------------------------------------------------
# 4. AUTO-GRAPH everything it can
# ------------------------------------------------------------------
def auto_graph(df: pd.DataFrame):
    numeric, dates, categorical = detect_types(df)
    print(f"📊 numeric={numeric}, dates={dates}, categorical={categorical}")

    if categorical and numeric:
        plot_bar(df, x=categorical[0], y=numeric[0])

    if dates and numeric:
        plot_line(df, x=dates[0], y=numeric[0])
    elif categorical and numeric:
        plot_line(df, x=categorical[0], y=numeric[0])

    if len(numeric) >= 2:
        plot_scatter(df, x=numeric[0], y=numeric[1])

    if numeric:
        plot_hist(df, numeric[0])

    plot_correlation(df)


# ------------------------------------------------------------------
# 5. MAIN
# ------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: python datagraph.py <file.xlsx> [sheet_name_or_index]")
        sys.exit(1)

    path = sys.argv[1]
    sheet = sys.argv[2] if len(sys.argv) > 2 else 0

    df = load_excel(path, sheet)
    auto_graph(df)
    print("\n✅ Done. Check the PNG files in this folder.")
    print("Built by TH-Hamza | Main author: TH-HAMZA")


if __name__ == "__main__":
    main()
