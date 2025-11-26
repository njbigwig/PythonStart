# Created by Copilot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pip install matplotlib
# pip install seaborn


# Load dataset (replace with your dataset path)
# Example: "all_space_missions.csv" from GitHub/Dynamic Duniya
#df = pd.read_csv("all_space_missions.csv") 
df = pd.read_csv("spacex_launches.csv")

# Inspect dataset
print(df.head())
print(df.columns)

# Ensure 'Year' column exists or extract from 'date_utc' column
if 'Year' not in df.columns:
    df['Date'] = pd.to_datetime(df['date_utc'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    
# Normalize mission status
if 'success' in df.columns:
    df['Mission_Status'] = df['success'].map({True: 'Success', False: 'Failure'})

# --- 1. Missions per year ---
missions_per_year = df.groupby('Year').size()

plt.figure(figsize=(12,6))
sns.lineplot(x=missions_per_year.index, y=missions_per_year.values, marker="o")
plt.title("Number of Space Missions per Year (1957 onwards)")
plt.xlabel("Year")
plt.ylabel("Number of Missions")
plt.grid(True)
plt.show()

# --- 2. Success vs Failure trends ---
status_per_year = df.groupby(['Year','Mission_Status']).size().unstack(fill_value=0)

plt.figure(figsize=(12,6))
status_per_year.plot(kind='line', marker="o")
plt.title("Mission Outcomes Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.legend(title="Mission Status")
plt.grid(True)
plt.show()

# --- 3. Missions by Country ---
if 'Country' in df.columns:
    missions_by_country = df['Country'].value_counts().head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=missions_by_country.values, y=missions_by_country.index, palette="viridis")
    plt.title("Top 10 Countries by Number of Space Missions")
    plt.xlabel("Number of Missions")
    plt.ylabel("Country")
    plt.show()

# --- 4. Cost Analysis (if available) ---
if 'Price' in df.columns:
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    avg_cost_per_year = df.groupby('Year')['Price'].mean()

    plt.figure(figsize=(12,6))
    sns.lineplot(x=avg_cost_per_year.index, y=avg_cost_per_year.values, marker="o", color="red")
    plt.title("Average Mission Cost Over Time")
    plt.xlabel("Year")
    plt.ylabel("Cost (Million USD)")
    plt.grid(True)
    plt.show()
