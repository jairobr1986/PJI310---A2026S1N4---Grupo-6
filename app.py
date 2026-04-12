import streamlit as st
from db import init_db, salvar_paciente, listar_pacientes
from utils import classificar_risco, formatar_imc

# 1. Configuração da página (Deve ser sempre o primeiro comando Streamlit)
st.set_page_config(page_title="Triagem Clínica Estética", page_icon="⚖️")
st.title("⚖️ Triagem de Risco Metabólico - Clínica Estética")

# Inicializa conexão com banco
conn = init_db()

# 2. Entrada de dados
st.header("Cadastro de Paciente")
with st.form("cadastro_paciente"):
    nome = st.text_input("Nome completo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso (kg)", min_value=10.0, max_value=300.0, step=0.1)
    with col2:
        altura = st.number_input("Altura (m)", min_value=0.5, max_value=2.5, step=0.01)

    submit = st.form_submit_button("Realizar Triagem")

    if submit:
        if nome and altura > 0:
            imc_atual = formatar_imc(peso, altura)
            risco = classificar_risco(peso, altura, idade)
            
            # Salva no banco de dados
            salvar_paciente(conn, (nome, idade, peso, altura, imc_atual, risco))
            
            # Alerta visual imediato
            if "VERMELHA" in risco:
                st.error(f"🚨 Paciente: {nome} | IMC: {imc_atual} | STATUS: {risco}")
            elif "AMARELO" in risco:
                st.warning(f"⚠️ Paciente: {nome} | IMC: {imc_atual} | STATUS: {risco}")
            else:
                st.success(f"✅ Paciente: {nome} | IMC: {imc_atual} | STATUS: {risco}")
        else:
            st.error("Por favor, preencha todos os campos corretamente.")

# 3. Consulta e Exibição
st.header("Fila de Atendimento")
df = listar_pacientes(conn)

if not df.empty:
    # Correção do erro: .applymap mudou para .map nas versões recentes do Pandas
    # Também usei use_container_width para a tabela ocupar a tela toda
    st.dataframe(
        df.style.map(
            lambda x: 'background-color: #ffcccc' if 'VERMELHA' in str(x) else 
                      'background-color: #ffffcc' if 'AMARELO' in str(x) else 
                      'background-color: #ccffcc' if 'VERDE' in str(x) else '',
            subset=['risco']
        ),
        use_container_width=True
    )
    
    # 4. Estatísticas
    st.subheader("📊 Perfil de Risco da Clínica")
    # Gráfico de barras simples com a contagem de cada risco
    contagem_risco = df["risco"].value_counts()
    st.bar_chart(contagem_risco)
else:
    st.info("Nenhum paciente registrado no momento.")