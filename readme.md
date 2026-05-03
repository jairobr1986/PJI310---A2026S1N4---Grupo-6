# 🩺 Triagem de Risco Metabólico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Sistema inteligente de triagem clínica focado em **UX Minimalista** e **Gestão de Fila por Prioridade**. O software automatiza o cálculo de IMC e organiza o fluxo de atendimento com base no risco metabólico e critérios de idade.

---

## 📸 Interface do Sistema

<div align="center">
  <p><b>Monitor de Chamada</b></p>
  <img src="assets/img/monitor_chamada.png" alt="Monitor de Chamada" width="800px">
  <br>
  <p><b>Fluxo de Cadastro</b></p>
  <img src="assets/img/novo_paciente.png" alt="Cadastro de pacientes" width="800px">
  <br>
  <p><b>Detalhamento Tecnico</b></p>
  <img src="assets/img/detalhamento_tecnico.png" alt="Cadastro de pacientes" width="800px">
</div>

---

## 📋 Funcionalidades Principais

* 🚀 **Fila Inteligente**: Ordenação automática priorizando idosos e casos de obesidade crítica.
* 🎨 **Monitor Minimalista**: Visual limpo com indicadores discretos (🔴, 🟡, 🟢) para reduzir a fadiga visual do operador.
* 🔍 **Detalhamento Técnico**: Seção expansível para profissionais de saúde consultarem dados biométricos detalhados sem poluir a tela principal.
* 🧮 **Cálculo Automático**: Classificação instantânea de Obesidade Grau I, II e III conforme os padrões de saúde.

## 🛠️ Estrutura do Projeto

```text
├── app.py           # Interface Streamlit e Lógica de UI
├── db.py            # Camada de Dados (SQLite + Pandas)
├── utils.py         # Motor de Cálculo e Regras de Negócio
└── README.md        # Documentação do Projeto