import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuración de la interfaz de la página web
st.set_page_config(
    page_title="Dashboard de Comportamiento del Cliente",
    page_icon="📊",
    layout="wide"
)

# Estilo CSS personalizado para mejorar el diseño de las tarjetas de métricas
st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: bold;
        color: #1f77b4;
    }
    div.css-1r6g72h {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Título principal
st.title("📊 Portal de Analítica: Comportamiento de Clientes")
st.markdown("Un análisis interactivo para identificar clientes VIP, retención y segmentación de mercado.")
st.markdown("---")

# 3. Ruta del archivo procesado
DATA_FILE = "clientes_procesados.csv"

# 4. Cargar el dataset procesado
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    st.error(f"No se encontró el archivo '{DATA_FILE}'. Asegúrate de haber ejecutado tu pipeline.ipynb primero.")
    st.stop()

# 5. Filtros dinámicos en la barra lateral (Sidebar)
st.sidebar.header("🔍 Filtros de Segmentación")

generos_disponibles = df['Gender'].unique()
generos_seleccionados = st.sidebar.multiselect(
    "Selecciona el Género:",
    options=generos_disponibles,
    default=generos_disponibles
)

segmentos_disponibles = df['Segmento'].unique()
segmentos_seleccionados = st.sidebar.multiselect(
    "Selecciona el Estado del Cliente:",
    options=segmentos_disponibles,
    default=segmentos_disponibles
)

# Aplicar filtros dinámicos
df_filtrado = df[
    (df['Gender'].isin(generos_seleccionados)) & 
    (df['Segmento'].isin(segmentos_seleccionados))
]

st.sidebar.success(f"Mostrando {len(df_filtrado):,} clientes basados en tus filtros.")

# ==========================================
# SECCIÓN DE MÉTRICAS CLAVE (KPIs)
# ==========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="👥 Clientes Seleccionados", 
        value=f"{len(df_filtrado):,}"
    )

with col2:
    ticket_promedio = df_filtrado['Monetary'].mean() if len(df_filtrado) > 0 else 0
    st.metric(
        label="💰 Valor de Vida Promedio (LTV)", 
        value=f"${ticket_promedio:,.2f}"
    )

with col3:
    frecuencia_promedio = df_filtrado['Frequency'].mean() if len(df_filtrado) > 0 else 0
    st.metric(
        label="🔄 Frecuencia de Compra", 
        value=f"{frecuencia_promedio:.1f} veces"
    )

with col4:
    tasa_churn = (df_filtrado['Churn'].sum() / len(df_filtrado)) * 100 if len(df_filtrado) > 0 else 0
    st.metric(
        label="📉 Tasa de Abandono (Churn)", 
        value=f"{tasa_churn:.1f}%"
    )

st.markdown("---")

# ==========================================
# SECCIÓN DE GRÁFICOS INTERACTIVOS
# ==========================================
col_grafico1, col_grafico2 = st.columns(2)

with col_grafico1:
    st.subheader("🎯 Distribución de Segmentos")
    
    # Agrupar datos para el gráfico
    segmento_counts = df_filtrado['Segmento'].value_counts().reset_index()
    segmento_counts.columns = ['Segmento', 'Cantidad']
    
    # Gráfico de barras interactivo
    fig_barras = px.bar(
        segmento_counts,
        x='Segmento',
        y='Cantidad',
        color='Segmento',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        template="plotly_dark"
    )
    fig_barras.update_layout(showlegend=False, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_barras, use_container_width=True)

with col_grafico2:
    st.subheader("🎂 Edad vs Valor Monetario")
    
    # Gráfico de dispersión interactivo
    fig_dispersion = px.scatter(
        df_filtrado,
        x='Customer Age',
        y='Monetary',
        color='Segmento',
        hover_name='Customer Name',
        opacity=0.6,
        color_discrete_sequence=px.colors.qualitative.Pastel,
        template="plotly_dark",
        labels={'Customer Age': 'Edad del Cliente', 'Monetary': 'Gasto Total ($)'}
    )
    fig_dispersion.update_layout(margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig_dispersion, use_container_width=True)