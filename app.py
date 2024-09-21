import streamlit as st
import pandas as pd

st.title("Visualizador de Datos CSV")

uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.table(df.head(10))

  # Crear datos
  
data = {
    "Índice": range(1, 11),
    "Nombre": [
        "Alice", "Bob", "Charlie", "David", "Eva",
        "Frank", "Grace", "Hannah", "Isaac", "Julia"
    ],
    "País": [
        "España", "México", "Argentina", "Colombia", "Chile",
        "Perú", "Venezuela", "Uruguay", "Bolivia", "Paraguay"
    ],
    "Género": [
        "Femenino", "Masculino", "Masculino", "Masculino", "Femenino",
        "Masculino", "Femenino", "Femenino", "Masculino", "Femenino"
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar la tabla en Streamlit
st.title("visualizador-datos-streamlit")
st.dataframe(df)  