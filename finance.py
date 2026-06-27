import pandas as pd
import streamlit as st
import plotly.express as px

print("my name")
st.markdown(
    "<h1 style='color:blue;'>Financial Analysis Dashboard</h1>",
    unsafe_allow_html=True
)

df=pd.read_excel(Product-Sales-Region.xlsx")
st.write(df.head())
fig = px.pie(
    df,
    names="Product",
    values="Quantity",
    title="Sales by Category",
    hole=0.3  # Optional: creates a donut chart
)

st.plotly_chart(fig, use_container_width=True)
