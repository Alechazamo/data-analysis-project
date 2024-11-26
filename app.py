import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')


show_histogram = st.checkbox('Mostrar histograma interactivo')

if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Histograma de Kilometraje (Odometer)")
    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_scatter:
    st.write('Creación de un gráfico de dispersión entre el kilometraje y el precio')
    fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Kilometraje vs Precio")
    st.plotly_chart(fig, use_container_width=True)


