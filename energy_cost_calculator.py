import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Energy Cost Calculator", page_icon="⚡")
st.title("⚡ Energy Cost Calculator with Graph")

st.markdown("Estimate your monthly electricity usage and cost.")

# Inputs
device = st.text_input("Device name", "Fan")
wattage = st.number_input("Power (Watts)", min_value=1, value=75)
hours = st.number_input("Usage per day (Hours)", min_value=0.0, value=4.0)
days = st.number_input("Days per month", min_value=1, value=30)
rate = st.number_input("Cost per kWh (₹)", min_value=1.0, value=7.0)

# Calculate
energy_kwh = (wattage * hours * days) / 1000
cost = energy_kwh * rate

# Output
st.subheader("📊 Estimated Usage")
st.write(f"*Energy Used:* {energy_kwh:.2f} kWh")
st.write(f"*Monthly Cost:* ₹{cost:.2f}")

if st.checkbox("Show yearly cost"):
    st.write(f"*Yearly Cost:* ₹{cost*12:.2f}")

# Graph
df = pd.DataFrame({
    'Category': ['Energy (kWh)', 'Monthly Cost (₹)'],
    'Value': [energy_kwh, cost]
})

fig = px.bar(df, x='Category', y='Value', color='Category', text='Value', title="Energy vs Cost")
st.plotly_chart(fig)
