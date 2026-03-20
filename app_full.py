import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Proyecto de Precios de Vehículos", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
    }

    h1, h2, h3, h4, h5, h6, p, div {
        color: white !important;
    }

    .stButton>button {
        background-color: #8000FF;
        color: white;
        border-radius: 10px;
    }

    .stMetric {
        background-color: rgba(255,255,255,0.1);
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


pd.set_option('display.max_columns', None)

# Título principal
st.title("🚗 Proyecto de Precios de Vehículos")

# Descripción / objetivo
st.markdown("""
### 🎯 Objetivo del Proyecto

El objetivo de este proyecto es tener más posibilidades de practicar las tareas habituales de la ingeniería de software.  
Gracias a estas tareas, podré aumentar y complementar mis habilidades en el campo de los datos.

Las tareas incluyen la creación y gestión de entornos virtuales de Python y el desarrollo de una aplicación web.

En este proyecto, proporcionamos un conjunto de datos de anuncios de venta de coches. Sin embargo, el enfoque no se centrará en el conjunto de datos ni en el análisis.
""")

# Separador visual
st.markdown("---")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Métricas rápidas (decorativo profesional)
st.subheader("📊 Resumen rápido del dataset")
col1, col2, col3 = st.columns(3)

col1.metric("Total de registros", len(car_data))
col2.metric("Precio promedio", f"${int(car_data['price'].mean())}")
col3.metric("Kilometraje promedio", f"{int(car_data['odometer'].mean())} km")

st.markdown("---")

# Botones
st.subheader("📈 Visualizaciones interactivas")

col_btn1, col_btn2 = st.columns(2)

hist_button = col_btn1.button('Construir histograma')
scatter_button = col_btn2.button('Construir gráfico de dispersión')

# Histograma
if hist_button:
    st.success('✔ Creación de un histograma para el conjunto de datos de coches')

    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del kilometraje",
    )

    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if scatter_button:
    st.success('✔ Creación de un diagrama de dispersión')

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre kilometraje y precio",
    )

    st.plotly_chart(fig, use_container_width=True)

# Pie de página decorativo
st.markdown("---")
st.caption(
    "📌 Aplicación desarrollada con Streamlit | Análisis exploratorio de datos de vehículos")