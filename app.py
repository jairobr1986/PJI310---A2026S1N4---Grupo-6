import streamlit as st
from db import init_db, salvar_paciente, listar_pacientes
from utils import classificar_risco

st.title("🏥 Sistema de Triagem Hospitalar (Mostruário)")

conn = init_db()

# Entrada de dados
st.header("Cadastro de Paciente")
nome = st.text_input("Nome do paciente")
temp = st.number_input("Temperatura (°C)", min_value=30.0, max_value=45.0, step=0.1)
fc = st.number_input("Frequência Cardíaca (bpm)", min_value=40, max_value=200)
pa = st.text_input("Pressão Arterial (ex: 120/80)")
fr = st.number_input("Frequência Respiratória (rpm)", min_value=10, max_value=40)
ox = st.number_input("Oxigenação (%)", min_value=70.0, max_value=100.0, step=0.1)

if st.button("Salvar paciente"):
    risco = classificar_risco(temp, fc, pa, fr, ox)
    salvar_paciente(conn, (nome, temp, fc, pa, fr, ox, risco))
    st.success(f"Paciente {nome} classificado como: {risco}")

# Consulta
st.header("Pacientes Registrados")
df = listar_pacientes(conn)
st.dataframe(df)

# Estatísticas rápidas
if not df.empty:
    st.subheader("📊 Estatísticas")
    st.write(df["risco"].value_counts())
