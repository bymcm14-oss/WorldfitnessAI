import streamlit as st
import base64
from IA import generar_rutina

st.set_page_config(
    page_title="WorldfitnessAI",
    page_icon="🏋️",
    layout="centered",
)

# ==========================================
# LOGO CENTRADO
# ==========================================

with open("assets/logo.png", "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{logo_base64}" width="120">
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# TÍTULO
# ==========================================

st.markdown(
    "<h1 style='text-align: center;'>WorldfitnessAI</h1>",
    unsafe_allow_html=True,
)

# ==========================================
# ESLOGAN
# ==========================================

st.markdown(
    "<p style='text-align: center; color: gray;'>Tu rutina personalizada en menos de un minuto.</p>",
    unsafe_allow_html=True,
)

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
    with st.spinner("🤖 Generando rutina personalizada..."):

        rutina = generar_rutina(
            objetivo,
            nivel,
            dias,
            tiempo
        )

    st.success("✅ ¡Rutina generada correctamente!")

    st.info(f"""
🎯 Objetivo: {objetivo}

💪 Nivel: {nivel}

📅 Días por semana: {dias}

⏱️ Tiempo por sesión: {tiempo}
""")
    st.subheader("📋 Tu rutina personalizada")

    st.write(rutina)