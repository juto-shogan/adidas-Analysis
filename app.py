from turtle import title, width
import pandas as pd
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(layout="wide")

df = pd.read_excel('/home/juto/Desktop/projects/adidas analysis/data/Adidas.xlsx')



# Graph1 
retailers = df['Retailer'].unique()
total_sales = df.groupby('Retailer')['TotalSales'].sum().reset_index()
colors = ['#3378e8']

# Plot Graph
plt.figure(figsize=(11,11))
fig1 = px.bar(data_frame=total_sales,
             x=total_sales.index,
             y='TotalSales',  
             color=retailers, 
             color_discrete_sequence=colors
)  # Use fig for plotly object

fig1.update_layout(width=800, height=600, margin=dict(l=50, r=50, b=50, t=50),
    title='Total Sales by Retailers',
    yaxis_title='Total Sales',
    xaxis_title='Retailers',
    xaxis=dict(
        tickvals=total_sales['Retailer']# Format tick labels with two decimal places and commas
    )
)


# graph2
# Convert 'InvoiceDate' to datetime format 
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceDate'] = df['InvoiceDate'].dt.strftime('%Y-%m')


# 2. Group data by year, month, etc. (choose your desired time granularity)
total_sales_over_time = df.groupby([df['InvoiceDate']])['TotalSales'].sum().reset_index()

# Create the plot
fig2= px.line(
    data_frame=total_sales_over_time,
    x='InvoiceDate',  # Replace with your time column name if different
    y='TotalSales',
    title='Total Sales Over Time'
)

# Customize the plot 
fig2.update_layout(
    title='Total Sales over Time',
    xaxis_title='Year',  # Adjust title based on your time granularity
    yaxis_title='Total Sales',
    xaxis_tickformat="%Y-%m"
)

# Graph3
units_sold_bystate = df.groupby('State')['UnitsSold'].sum().sort_index()
unitTotal = units_sold_bystate.to_frame(name='State')
grand_df= df.groupby('State')[['TotalSales','UnitsSold']].sum().sort_index()

plt.figure(figsize=(11,15))

# Create traces for fig3
trace1 = go.Bar(
    x=grand_df.index,
    y=grand_df['TotalSales'],
    name='Total Sales',
    marker_color='royalblue'
)

trace3 = go.Scatter(
    # x=grand_df.index,
    # y=grand_df['UnitsSold'],
    x=unitTotal.index,
    y=unitTotal['State'],
    name='Units Sold',
    line_color='orange',
    marker_opacity=0,
    yaxis='y2'
    # Hide markers for cleaner line
)

# Combine traces into fig3
fig3 = go.Figure(data=[trace1, trace3])

fig3.update_layout(
    title='Total Sales and Units Sold by State',
    xaxis_title='State',
    xaxis_tickangle=-45,
    yaxis_title='Total Sales (Millions)',  # Label for primary y-axis
    yaxis2=dict(
        title='Units Sold (Thousands)',  # Label for secondary y-axis
        overlaying='y',
        side='right'
    )   
)


# Graph 4
fig4 = px.treemap(df, path=['Region', 'City'], 
                 values='TotalSales',
                color='City',  # Color nodes by region
                hover_name='TotalSales',
                hover_data=['TotalSales'],  # Show relevant data on hover
                title='Total Sales by Region and City',
                color_discrete_sequence=['pink', 'red', 'green', 'orange', 'blue', 'purple']
            )  # Customize color palette
fig4.update_traces(textinfo="label+value")
fig4.update_layout(margin=dict(t=50, l=50, r=50, b=50))  # Adjust margins for better readability


# st.title("Adidas Interactive Sales Dashboard")



col1, col2, col3, col4= st.columns([1,2,3,4])



with st.container():
    
    with col1:
        st.image('/home/juto/Desktop/projects/adidas analysis/logo.jpeg', width=150)
    
    with col2:
        st.title("Adidas Interactive Sales Dashboard")
    
with col3:
    # st.plotly_chart(fig1, use_)
    st.plotly_chart(fig1, use_container_width=True)   
    st.expander("Retailer wise Sales")
    st.dataframe(total_sales)
    

with col4:
    st.plotly_chart(fig2, use_container_width=True)    
    

st.plotly_chart(fig3, use_container_width=True)  

st.plotly_chart(fig4, use_container_width=True)


