import pandas as pd
import streamlit as st

# Daten laden
df = pd.read_csv("data.csv")

# Datum verarbeiten
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# KPIs berechnen
total_revenue = df["revenue"].sum()
avg_revenue = df["revenue"].mean()

# Dashboard Titel
st.title("AI Reporting Dashboard")

# KPIs anzeigen
st.metric("Total Revenue", total_revenue)
st.metric("Average Revenue", round(avg_revenue, 2))

# Diagramm anzeigen
st.line_chart(df["revenue"])