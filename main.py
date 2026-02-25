import streamlit as st

# Configuración y Título
st.set_page_config(page_title="DS Canet", page_icon="🛡️")
st.title("🛡️ DS: Diagnóstico Seguro")
st.caption("Edición Especial: Canet de Berenguer")

# --- NUEVA FUNCIÓN DE VOZ ---
st.subheader("🎤 Dictar informe del caso")
audio_value = st.audio_input("Pulsa para hablar (Hacienda, SEPE, situación familiar...)")

if audio_value:
    st.success("✅ Audio recibido. Analizando datos técnicos...")

# --- FORMULARIO DE DATOS ---
with st.container(border=True):
    nombre = st.text_input("Nombre del Usuario")
    miembros = st.number_input("Nº Miembros Unidad Convivencia", min_value=1, value=1)
    ingresos = st.number_input("Ingresos Totales Mensuales (€)", min_value=0.0, step=10.0)

# --- LÓGICA DE DIAGNÓSTICO ---
if ingresos > 0:
    st.divider()
    st.subheader("📊 Pre-Diagnóstico")
    st.info(f"Analizando ingresos de {ingresos}€ para {miembros} personas según baremos de Canet...")
    
