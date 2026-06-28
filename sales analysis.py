import pandas as pd
import streamlit as st
import plotly.express as px

st.markdown("<h1 style='color:blue;'>Sales Analysis Dashboard</h1>", unsafe_allow_html=True )
#import the sales Data
df=pd.read_excel("Product-Sales-Region.xlsx")

#Add calculated colums into the dataframe
df["Month"] = pd.to_datetime(df["OrderDate"]).dt.strftime("%b")

#Exploratory Data Analysis
st.write(df.head())
#Create a Pie chart of Sales by Product Category
fig = px.pie(df, names="Product", values="Quantity", title="Sales by Category",
    hole=0.3  )

#Line Chart
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df["Month"] = pd.Categorical(df["Month"],categories=month_order,ordered=True)
trend = df.groupby("Month", observed=False)["TotalPrice"].sum().reset_index()
fig2 = px.line(trend,x="Month",y="TotalPrice",markers=True,title="Monthly Sales Trend")

#render the charts into the Streamlit Layout
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
