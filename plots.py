# This script generates plots to visualize outliers in the voting data for Nawrocki and Trzaskowski.
# It uses linear regression to identify outliers based on the relationship between votes in the second round and the przepływy votes.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

def get_outliers(df, x_col, y_col, threshold=8):
    """
    Identify outliers in the dataset based on a linear regression model.
    Outliers are defined as points where the residuals exceed a specified threshold
    times the standard deviation of the residuals.
    Parameters:
    - df: DataFrame containing the data.
    - x_col: Name of the column to use as the independent variable.
    - y_col: Name of the column to use as the dependent variable.
    - threshold: Number of standard deviations to use for outlier detection.
    Returns:
    - outlier_mask: Boolean Series indicating which points are outliers.    
    - residuals: The residuals from the linear regression model.
    """
    # Drop rows where either x or y is NaN
    df_clean = df[[x_col, y_col]].dropna()
    x = df_clean[x_col].values.reshape(-1, 1)
    y = df_clean[y_col].values
    model = LinearRegression().fit(x, y)
    y_pred = model.predict(x)
    residuals = y - y_pred
    std = np.std(residuals)
    outlier_mask = np.abs(residuals) > threshold * std
    print(threshold*std, ' is a standard deviation threshold for outliers.')
    print(f"Number of outliers detected for {x_col} vs {y_col}: {np.sum(outlier_mask)}")
    print(f"Outliers detected: {df_clean[outlier_mask].shape[0]} out of {df_clean.shape[0]} total points.")
    # Create a boolean mask aligned with the original df index, False for dropped rows
    outlier_mask_full = pd.Series(False, index=df.index)
    outlier_mask_full.loc[df_clean.index] = outlier_mask

    return outlier_mask_full, residuals

df_result=pd.read_excel(os.path.join("result","results_all.xlsx"))

def plot_outliers():
    """
    Generate plots to visualize outliers in the voting data for Nawrocki and Trzaskowski.
    It uses linear regression to identify outliers based on the relationship between votes in the second round
    and the przepływy votes.
    """
    print("Generating plots for outliers in voting data...")

    naw_outliers, naw_residuals = get_outliers(df_result, "nawrocki_2", "nawrocki_przeplywy_2_n")
    df_result["nawrocki_outlier"] = naw_outliers
    
    trz_outliers, trz_residuals = get_outliers(df_result, "trzaskowski_2", "trzaskowski_przeplywy_2_n")
    df_result["trzaskowski_outlier"] = trz_outliers

    both_outliers = df_result["nawrocki_outlier"] & df_result["trzaskowski_outlier"]

    print("Results where both Nawrocki and Trzaskowski are outliers:")
    print(df_result[both_outliers][["komisja",
        "nawrocki_2", "nawrocki_przeplywy_2_n", 
        "trzaskowski_2", "trzaskowski_przeplywy_2_n"
    ]])

    # === Plot ===
    plt.style.use("seaborn-darkgrid")
    sns.set_context("talk")
    sns.set_palette("deep")
    sns.set_style("whitegrid")   

    plt.figure(figsize=(12, 5))

    # Nawrocki 
    plt.subplot(1, 2, 1)
    sns.regplot(
        data=df_result,
        x="nawrocki_2",
        y="nawrocki_przeplywy_2_n",
        color="blue",
        line_kws={"color": "black", "lw": 1}
    )
    sns.scatterplot(
        data=df_result[naw_outliers],
        x="nawrocki_2",
        y="nawrocki_przeplywy_2_n",
        color="orange",
        label="Outliers"
    )
    plt.title("Nawrocki: Round II Votes vs Przepływy")
    plt.xlabel("Votes in Round II")
    plt.ylabel("Przepływy Votes")

    # Trzaskowski
    plt.subplot(1, 2, 2)
    sns.regplot(
        data=df_result,
        x="trzaskowski_2",
        y="trzaskowski_przeplywy_2_n",
        color="red",
        line_kws={"color": "black", "lw": 1}
    )
    sns.scatterplot(
        data=df_result[trz_outliers],
        x="trzaskowski_2",
        y="trzaskowski_przeplywy_2_n",
        color="orange",
        marker=".",
        label="Outliers"
    )
    plt.title("Trzaskowski: Round II Votes vs Przepływy")
    plt.xlabel("Votes in Round II")
    plt.ylabel("Przepływy Votes")

    plt.tight_layout()
    plt.savefig("result/votes_vs_przeplywy_outliers.png")
    plt.close()

    print("Plot with outliers saved as result/votes_vs_przeplywy_outliers.png\n")


if __name__ == "__main__":
    plot_outliers()
    print("Plots generated successfully.")

