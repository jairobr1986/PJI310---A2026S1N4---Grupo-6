import streamlit as st
from db import init_db, salvar_paciente, listar_pacientes
from utils import classificar_risco, formatar_imc

st.set_page_config(page_title="Triagem Clínica", page_icon="🩺", layout="wide")

# CSS para métricas e espaçamento
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #1e3a8a; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🩺 Triagem de Risco Metabólico")
conn = init_db()

tab_fila, tab_cadastro = st.tabs(["📋 Fila de Chamada", "➕ Novo Paciente"])

with tab_cadastro:
    st.subheader("Dados do Paciente")
    with st.form("form_clinica", clear_on_submit=True):
        nome = st.text_input("Nome completo")
        idade = st.number_input("Idade", min_value=0, value=30)
        c1, c2 = st.columns(2)
        with c1: peso = st.number_input("Peso (kg)", min_value=1.0, step=0.1, value=70.0)
        with c2: altura = st.number_input("Altura (m)", min_value=0.5, step=0.01, value=1.70)
        
        if st.form_submit_button("Finalizar Triagem", use_container_width=True):
            if nome:
                status, nivel, classe = classificar_risco(peso, altura, idade)
                salvar_paciente(conn, (nome, idade, peso, altura, formatar_imc(peso, altura), status, nivel, classe))
                st.toast(f"✅ {nome} na fila!", icon='🩺')
                st.rerun()

with tab_fila:
    df = listar_pacientes(conn)
    
    if not df.empty:
        # 1. CRIAÇÃO DA POSIÇÃO MINIMALISTA
        # Extrai o emoji do risco para colocar ao lado do número
        df_display = df.reset_index(drop=True)
        df_display['Emoji'] = df_display['risco'].str[0] # Pega o 🔴, 🟡 ou 🟢
        df_display['Posição'] = (df_display.index + 1).astype(str) + "º " + df_display['Emoji']

        # 2. MONITOR DE CHAMADA (VISÃO LIMPA)
        st.subheader("📢 Monitor de Chamada")
        monitor_df = df_display[['Posição', 'nome', 'classificacao', 'risco']].copy()
        
        # Exibe a tabela sem fundos coloridos agressivos
        st.dataframe(
            monitor_df.drop(columns=['Emoji'], errors='ignore'),
            use_container_width=True, 
            hide_index=True
        )

        # 3. DETALHAMENTO TÉCNICO
        st.write("")
        with st.expander("🔍 Detalhamento Técnico"):
            tecnico_df = df_display[['Posição', 'nome', 'idade', 'peso', 'altura', 'imc']]
            st.dataframe(
                tecnico_df.style.format({'peso': '{:.1f} kg', 'altura': '{:.2f} m', 'imc': '{:.2f}'}),
                use_container_width=True, 
                hide_index=True
            )
        
        # MÉTRICAS
        st.divider()
        m1, m2 = st.columns(2)
        m1.metric("Total na Fila", len(df))
        m2.metric("Prioridades", len(df[df['risco'].str.contains('🔴')]))
    else:
        st.info("Fila vazia.")