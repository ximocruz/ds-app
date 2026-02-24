import streamlit as st

st.set_page_config(page_title="DS - Diagnóstico Seguro", page_icon="🛡️")

st.title("🛡️ DS: Diagnóstico Seguro")
st.subheader("Edición Canet de Berenguer")

# --- PANEL DE CONTROL (ADMIN) ---
with st.sidebar:
    st.header("Configuración")
    iprem = st.number_input("IPREM Mensual (Umbral)", value=600)
    pei_min = st.number_input("PEI Mínimo", value=210)
    pei_max = st.number_input("PEI Máximo", value=420)

# --- ENTRADA DE DATOS ---
st.info("Introduce los datos del usuario para el diagnóstico")
col1, col2 = st.columns(2)

with col1:
    nombre = st.text_input("Nombre del Usuario")
    miembros = st.number_input("Nº Miembros Unidad Convivencia", min_value=1, value=1)
    nie = st.checkbox("¿Tiene NIE / Residencia Legal?")

with col2:
    ingresos = st.number_input("Ingresos Totales Mensuales (€)", min_value=0.0)
    alquiler = st.number_input("Gasto Alquiler/Hipoteca (€)", min_value=0.0)

# --- LÓGICA DE CÁLCULO ---
rpc = ingresos / miembros
es_apto_pei = rpc <= iprem

# --- RESULTADOS ---
st.divider()
st.header("📋 Diagnóstico de Ayudas")

if es_apto_pei:
    st.success(f"✅ APTO para PEI Canet (RPC: {rpc:.2f}€)")
    # Simulación de baremación simple
    cuantia = pei_max if rpc < (iprem/2) else pei_min
    st.metric("Propuesta Económica PEI", f"{cuantia} €")
else:
    st.error(f"❌ NO APTO para PEI (RPC: {rpc:.2f}€ supera el umbral de {iprem}€)")

# --- BLOQUES ADICIONALES ---
st.subheader("Otras Prestaciones")
if not nie:
    st.warning("⚠️ Sin NIE: IMV bloqueado. Priorizar RVI (Exclusión).")
else:
    st.info("✅ Apto para estudio de IMV y Subsidios SEPE.")

if st.button("Generar Borrador de Informe"):
    st.write(f"Generando documento para {nombre}...")
    st.download_button("Descargar PDF (Simulado)", "Contenido del informe...", file_name="informe_ds.pdf")
