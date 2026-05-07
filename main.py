import pandas as pd

# Daten laden
df = pd.read_csv("data.csv")

# KPIs berechnen
total_revenue = df["revenue"].sum()
avg_revenue = df["revenue"].mean()

print("Total Revenue:", total_revenue)
print("Average Revenue:", avg_revenue)