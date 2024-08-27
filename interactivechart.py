import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('question3.csv')

def adjust_size(size_series, min_size, max_size):
    min_val = size_series.min()
    max_val = size_series.max()
    return min_size + (size_series - min_val) / (max_val - min_val) * (max_size - min_size)

df['adjusted_size'] = adjust_size(df['avg_ratings_average'], 1, 10)

fig = px.scatter(
    df,
    x='name',  
    y='total_ratings_count',  
    size='adjusted_size',  
    color='avg_ratings_average',  
    hover_name='name',  
    hover_data={'name': True, 'total_ratings_count': True, 'avg_ratings_average': True},
    title='Number of Awards by Winery',
    labels={'total_ratings_count': 'Total Awards', 'avg_ratings_average': 'Average Rating', 'name': 'Winery'},
    color_continuous_scale='Viridis'
)

fig.update_layout(
    xaxis_title='Winery',
    yaxis_title='Total Awards',
    xaxis_tickangle=-45,
    showlegend=True
)

st.title('Interactive Winery Awards ')
st.plotly_chart(fig)
