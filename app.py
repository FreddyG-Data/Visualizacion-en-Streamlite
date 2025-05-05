import streamlit as st
import pandas as pd
import requests

# Título del dashboard
st.title("🚪 Entradas al Club")

# URL de tu API
API_URL = "https://99e5-181-129-180-130.ngrok-free.app/entradas"

# Llama a la API
try:
    response = requests.get(API_URL)
    data = response.json()
    
    # Convierte a DataFrame
    df = pd.DataFrame(data)
    
    # Muestra los datos en tabla
    st.subheader("📋 Tabla de registros")
    st.dataframe(df)

    # Filtros (ejemplo: por fecha)
    fechas = df["fecha_entrada"].unique()
    fecha_filtrada = st.selectbox("Filtrar por fecha", sorted(fechas, reverse=True))
    df_filtrado = df[df["fecha_entrada"] == fecha_filtrada]

    st.subheader(f"🔎 Registros para {fecha_filtrada}")
    st.dataframe(df_filtrado)

except Exception as e:
    st.error("No se pudo conectar a la API")
    st.text(str(e))
