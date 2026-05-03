# 🩺 Triagem de Risco Metabólico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Sistema inteligente de triagem clínica focado em **UX Minimalista** e **Gestão de Fila por Prioridade**. Desenvolvido para automatizar o cálculo de IMC e organizar o atendimento com base no risco metabólico e idade.

---

## 📸 Interface do Sistema

> **Dica:** Adicione aqui um print da sua tela "Monitor de Chamada". Você pode salvar a imagem na pasta do projeto e linkar assim:
> `![Monitor de Chamada](assets\img\monitor_chamada.png)`
> `![Cadastro de pacientes](assets\img\assets\img\novo_paciente.png)`

---

## 📋 Funcionalidades Principais

*   **Fila Inteligente**: Ordenação automática (Idosos + Obesidade Crítica primeiro).
*   **Monitor Minimalista**: Visual limpo com indicadores discretos (🔴, 🟡, 🟢) para evitar fadiga visual.
*   **Detalhamento Técnico**: Seção expansível para profissionais de saúde consultarem dados biométricos.
*   **Cálculo Automático**: Classificação instantânea de Obesidade Grau I, II e III.

## 🛠️ Estrutura do Projeto

```text
├── app.py           # Interface Streamlit e Lógica de UI
├── db.py            # Camada de Dados (SQLite + Pandas)
├── utils.py         # Motor de Cálculo e Regras de Negócio
└── README.md        # Documentação do Projeto