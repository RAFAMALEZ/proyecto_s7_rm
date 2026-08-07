import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Titulo
st.header('Visor de datos', divider = "gray")

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        color_discrete_sequence=['orange']
        )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear una casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # Si la casilla está marcada
    st.write('Creación de un gráfico de dispersión entre el precio y el kilometraje (odometer)')
    
    # Crear gráfico de dispersión: Precio vs. Kilometraje
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color_discrete_sequence=['green']
        )
    
    # Mostrar gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
    