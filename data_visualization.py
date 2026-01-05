"""
Weather Data Analysis Project
-----------------------------
Complete data analysis pipeline:
Load → Clean → Analyze → Visualize → Report

Dataset: weather.csv
Author: Harshvardhan Borgohain
"""

import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------
# Data Loading
# -------------------------------------------------

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load weather dataset from CSV file.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("❌ weather.csv not found. Check file path.")


# -------------------------------------------------
# Data Exploration
# -------------------------------------------------

def explore_data(df: pd.DataFrame) -> None:
    """
    Display basic dataset information.
    """
    print("\n📊 DATASET OVERVIEW")
    print(df.head())
    print("\n📌 Dataset Shape:", df.shape)
    print("\n📌 Data Types")
    print(df.dtypes)
    print("\n📌 Missing Values")
    print(df.isnull().sum())


# -------------------------------------------------
# Data Cleaning
# -------------------------------------------------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset by handling missing values
    and formatting date column.
    """
    df = df.drop_duplicates()

    # Convert date column
    df["Date.Full"] = pd.to_datetime(df["Date.Full"], errors="coerce")

    # Fill missing numeric values with mean
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Fill missing text values
    text_cols = df.select_dtypes(include="object").columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    return df


# -------------------------------------------------
# Analysis
# -------------------------------------------------

def calculate_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate key weather statistics.
    """
    metrics = {
        "avg_temperature": df["Data.Temperature.Avg Temp"].mean(),
        "max_temperature": df["Data.Temperature.Max Temp"].max(),
        "min_temperature": df["Data.Temperature.Min Temp"].min(),
        "total_precipitation": df["Data.Precipitation"].sum(),
        "avg_wind_speed": df["Data.Wind.Speed"].mean()
    }
    return metrics


# -------------------------------------------------
# Visualization
# -------------------------------------------------

def plot_temperature_trend(df: pd.DataFrame) -> None:
    """
    Line chart for average temperature over time.
    """
    plt.figure()
    plt.plot(df["Date.Full"], df["Data.Temperature.Avg Temp"])
    plt.xlabel("Date")
    plt.ylabel("Average Temperature (°F)")
    plt.title("Average Temperature Trend Over Time")
    plt.show()


def plot_monthly_precipitation(df: pd.DataFrame) -> None:
    """
    Bar chart for average monthly precipitation.
    """
    monthly_precip = df.groupby("Date.Month")["Data.Precipitation"].mean()

    plt.figure()
    monthly_precip.plot(kind="bar")
    plt.xlabel("Month")
    plt.ylabel("Average Precipitation")
    plt.title("Average Monthly Precipitation")
    plt.show()


# -------------------------------------------------
# Reporting
# -------------------------------------------------

def generate_report(metrics: dict) -> None:
    """
    Print formatted analysis report.
    """
    print("\n🌦️ WEATHER ANALYSIS REPORT")
    print("=" * 45)
    print(f"🌡️ Average Temperature: {metrics['avg_temperature']:.2f} °F")
    print(f"🔥 Maximum Temperature: {metrics['max_temperature']:.2f} °F")
    print(f"❄️ Minimum Temperature: {metrics['min_temperature']:.2f} °F")
    print(f"🌧️ Total Precipitation: {metrics['total_precipitation']:.2f}")
    print(f"💨 Average Wind Speed: {metrics['avg_wind_speed']:.2f}")
    print("=" * 45)
    print("✅ Analysis completed successfully.\n")


# -------------------------------------------------
# Main Execution
# -------------------------------------------------

def main():
    file_path = "weather.csv"

    df = load_data(file_path)
    explore_data(df)

    df = clean_data(df)
    metrics = calculate_metrics(df)

    generate_report(metrics)
    plot_temperature_trend(df)
    plot_monthly_precipitation(df)


if __name__ == "__main__":
    main()
