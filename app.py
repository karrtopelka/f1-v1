import streamlit as st
import pandas as pd

st.title('🏎️ F1 Race Predictor Dashboard')

# Load or collect data
# For now, we'll load the historical data
historical_results = pd.read_csv('data/historical_results.csv')

# Display data
st.header('Historical Results')
st.write(historical_results)

# Add more components as you develop them
