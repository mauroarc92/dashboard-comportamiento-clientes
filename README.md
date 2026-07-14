# Análisis de Comportamiento del Cliente

## Presentación del proyecto
Este proyecto es un dashboard interactivo de analítica de clientes desarrollado con Streamlit. Su objetivo es explorar y visualizar el comportamiento de los clientes a partir de un dataset procesado, permitiendo identificar segmentos, valores de vida del cliente (LTV), frecuencia de compra y tasa de churn.

## Características principales
- Visualización interactiva de segmentos de clientes.
- Net métricas clave (clientes seleccionados, LTV promedio, frecuencia de compra y churn).
- Filtros dinámicos por género y segmento de cliente.
- Gráficos interactivos con Plotly para análisis de distribución y comportamiento.

## Archivos del proyecto
- `app.py`: aplicación principal de Streamlit.
- `clientes_procesados.csv`: dataset procesado usado por la app.
- `pipeline.ipynb`: notebook de procesamiento y transformación de datos.
- `requirements.txt`: dependencias del proyecto.

## Requisitos
- Python 3.8 o superior.
- Streamlit
- pandas
- plotly

## Instalación
1. Crear y activar un entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución
Ejecuta la app de Streamlit desde la carpeta del proyecto:

```bash
streamlit run app.py
```

Luego abre la dirección local que Streamlit indique en el navegador.

## Notas
- La app usa el archivo `clientes_procesados.csv`. Si no existe, muestra un mensaje de error y detiene la ejecución.
- Se recomienda ejecutar primero `pipeline.ipynb` para generar y validar el dataset procesado.

## Objetivo
Facilitar el análisis de clientes y la toma de decisiones con una interfaz sencilla y visual. El proyecto está pensado para identificar patrones de consumo, segmentos prioritarios y posibles riesgos de pérdida de clientes.
