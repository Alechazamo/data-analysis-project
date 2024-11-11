import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos
df = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title("Análisis Exploratorio de Vehículos")

# Crear y mostrar un histograma
st.subheader("Histograma del odómetro")
fig_hist = px.histogram(df, x="odometer")
st.plotly_chart(fig_hist)

# Crear y mostrar un gráfico de dispersión
st.subheader("Gráfico de Dispersión: Odómetro vs Precio")
fig_scatter = px.scatter(df, x="odometer", y="price")
st.plotly_chart(fig_scatter)
