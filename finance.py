import pandas as pd
import streamlit as st
import plotly.express as px

st.markdown("<h1 style='color:blue;'>Financial Analysis Dashboard</h1>", unsafe_allow_html=True )
#import the sales Data
df=pd.read_excel("Product-Sales-Region.xlsx")

#Add calculated colums into the dataframe
df["Month"] = pd.to_datetime(df["OrderDate"]).dt.strftime("%b")

#Exploratory Data Analysis
st.write(df.head())
#Create a Pie chart of Sales by Product Category
fig = px.pie(df, names="Product", values="Quantity", title="Sales by Category",
    hole=0.3  )
fig2 = px.line(trend,x="Month",y="Sales",markers=True,title="Monthly Sales Trend")

#render the charts into the Streamlit Layout
st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
