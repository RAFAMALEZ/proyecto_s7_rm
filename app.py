import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Uso de caché para optimizar la velocidad de carga de la aplicación web
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    
    # Limpieza de nulos aplicada directamente al cargar
    df['is_4wd'] = df['is_4wd'].fillna(0.0)
    df['paint_color'] = df['paint_color'].fillna('unknown')
    df['model_year'] = df['model_year'].fillna(df.groupby('model')['model_year'].transform('median'))
    df['cylinders'] = df['cylinders'].fillna(df.groupby('model')['cylinders'].transform('median'))
    df['odometer'] = df['odometer'].fillna(df.groupby('model')['odometer'].transform('median'))
    
    # Filtrar precios atípicos y limpiar nulos restantes
    df_cleaned = df[df['price'] >= 100].copy()
    df_cleaned = df_cleaned.dropna(subset=['odometer'])
    
    # Creación de la columna 'manufacturer' extrayendo la primera palabra del modelo
    df_cleaned['manufacturer'] = df_cleaned['model'].apply(lambda x: x.split()[0])
    
    return df_cleaned

car_data = load_data()

# Encabezado principal
st.header('Visor de datos de Vehículos Usados', divider="gray")


# --- 1. VISOR DE DATOS CON FILTRO ---
st.subheader("Exploración del conjunto de datos")
excluir_pequenos = st.checkbox("Excluir fabricantes con menos de 1000 anuncios")

if excluir_pequenos:
    # Lógica: Filtrar marcas utilizando value_counts
    conteo_marcas = car_data['manufacturer'].value_counts()
    marcas_validas = conteo_marcas[conteo_marcas > 1000].index
    datos_mostrar = car_data[car_data['manufacturer'].isin(marcas_validas)]
else:
    datos_mostrar = car_data

# Mostrar la tabla controlada por la casilla de verificación
st.dataframe(datos_mostrar)

st.divider()


# --- 2. GRÁFICOS APILADOS POR CATEGORÍA ---
st.subheader("Distribución de kilometraje y precio")
build_hist = st.checkbox('Construir histograma de kilometraje apilado')

if build_hist:
    # Lógica: Histograma con el parámetro color para apilar bloques
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        color="condition", 
        labels={'odometer': 'Kilometraje (millas)', 'condition': 'Condición del vehículo'},
        title="Distribución del Kilometraje por Condición"
    )
    fig_hist.update_layout(yaxis_title="Cantidad de vehículos")
    st.plotly_chart(fig_hist, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión (Precio vs. Kilometraje)')

if build_scatter:
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="type", # Apilamiento de color por tipo de vehículo
        labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio ($)', 'type': 'Tipo de carrocería'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()


# --- 3. COMPARADOR DINÁMICO DE PRECIOS ---
st.subheader("Comparador dinámico de precios entre fabricantes")

# Capturar lista de fabricantes únicos
fabricantes = sorted(car_data['manufacturer'].unique())

# Lógica: Variables con menús desplegables para selección del usuario
col1, col2 = st.columns(2)
with col1:
    marca1 = st.selectbox("Selecciona la primera marca", options=fabricantes, index=fabricantes.index('ford') if 'ford' in fabricantes else 0)
with col2:
    marca2 = st.selectbox("Selecciona la segunda marca", options=fabricantes, index=fabricantes.index('chevrolet') if 'chevrolet' in fabricantes else 1)

normalizar = st.checkbox("Normalizar gráfico (mostrar porcentajes)")

# Lógica: Filtrar el DataFrame para las dos marcas seleccionadas
datos_comparacion = car_data[car_data['manufacturer'].isin([marca1, marca2])]

# Construir el gráfico superpuesto
fig_comp = px.histogram(
    datos_comparacion,
    x="price",
    color="manufacturer",
    barmode="overlay", # Parámetro para superponer distribuciones
    histnorm='percent' if normalizar else None, # Parámetro para normalizar los datos
    labels={'price': 'Precio ($)', 'manufacturer': 'Marca'},
    title=f"Comparación de precios: {marca1.capitalize()} vs {marca2.capitalize()}"
)
st.plotly_chart(fig_comp, use_container_width=True)
