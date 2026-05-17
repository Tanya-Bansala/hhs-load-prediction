import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard Title
st.title("UAC Predictive Care Forecasting Dashboard")

# Load CSV
df = pd.read_csv("forecast_results.csv")

# Show column names
st.subheader("Column Names")
st.write(df.columns)

# Show dataset
st.subheader("Forecast Data")
st.write(df.head())

# Graph
st.subheader("Forecast Graph")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    df.iloc[:,0],
    df.iloc[:,1]
)

plt.xticks(rotation=45)

st.pyplot(fig)