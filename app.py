import streamlit as st

st.set_page_config(
    page_title="WorldfitnessAI",
    page_icon="🏋️",
    layout="centered",
)

col1, col2 = st.columns([4, 1])

with col1:
    st.title("WorldfitnessAI")
    st.caption("Tu rutina personalizada en menos de un minuto.")

with col2:
    st.write("🏋️")
    
st.divider()

st.subheader("👋 ¡Bienvenido!")

st.write(
    "Responde las siguientes preguntas para generar una rutina personalizada."
)
objetivo = st.selectbox(
    "¿Cuál es tu objetivo principal?",
    [
        "Ganar masa muscular",
        "Perder grasa",
        "Aumentar fuerza",
        "Mejorar condición física",
    ]
)
st.write("Tu objetivo es:", objetivo)

nivel = st.selectbox(
    "¿Cuál es tu nivel actual de experiencia entrenando?",
    [
        "Principiante (0-6 meses)",
        "Intermedio (6 meses - 2 años)",
        "Avanzado (2-5 años)",
        "Experto (+5 años)",
        
    ]
)
st.write("Tu nivel de experiencia es:", nivel)

dias = st.slider(
    "¿Cuántos días a la semana puedes entrenar?",
    min_value=1,
    max_value=7,
    value=4,
    
)
st.write("Has seleccionado entrenar", dias, "días a la semana.")

tiempo = st.select_slider(
    "¿Cuánto tiempo puedes dedicar a cada entrenamiento?",
    options=["30 min", "45 min", "60 min", "90 min", "+90 min"]
)
st.write("Tiempo disponible por sesión:", tiempo)
st.divider()

if st.button("🏋️ Generar rutina", use_container_width=True):
    with st.spinner("Generando rutina personalizada..."):
        import time
        time.sleep(3)

    st.success("✅ ¡Rutina generada correctamente!")