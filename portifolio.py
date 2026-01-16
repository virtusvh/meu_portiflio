abrir = 'streamlit run portifolio.py'

import streamlit as st
import pandas as pd
import plotly

# Configuração da Página
st.set_page_config(page_title="Portfólio de Automação e Dados", layout="wide")

# Estilo Personalizado para "Cards"
st.markdown("""
    <style>
    .main { background-color: #F0F2F6; }
    .stCard {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Barra Lateral (Menu de Navegação)
st.sidebar.title("Navegação")
aba = st.sidebar.radio("Ir para:", ["Sobre Mim", "Automações (Vídeos)", "Dashboards Interativos"])

# --- ABA: SOBRE MIM ---
if aba == "Sobre Mim":
    st.title("Olá, eu sou um Especialista em Automação e Dados 🚀")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", caption="Tua Foto ou Logo")  # Substitui pela imagem
    with col2:
        st.write("""
        Especialista em criar soluções robustas com **Python, Pandas e Selenium e agentes de IA**. 
        Focado em reduzir o trabalho manual e transformar dados brutos em decisões estratégicas.

        **Habilidades Principais:**
        - Automação RPA (Selenium, IxBrowser, APIs)
        - ETL e Limpeza de Dados (Pandas, Openpyxl)
        - Dashboards Interativos (Streamlit, Plotly)
        """)

# --- ABA: AUTOMAÇÕES (VÍDEOS) ---
elif aba == "Automações (Vídeos)":
    st.title("Projetos de Automação")
    st.write("Demonstrações em vídeo de robôs a trabalhar em tempo real.")

    # Projeto 1: IxBrowser
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            # Substitui pelo link do teu vídeo (YouTube/Vimeo/Loom)
            st.video("https://www.youtube.com/watch?v=Exemplo")
        with col2:
            st.subheader("Automação IxBrowser")
            st.write("App Desktop que lê URLs de um Excel e gere múltiplos perfis anónimos.")
            st.info("Tecnologias: Python, Selenium, API IxBrowser, Pandas.")
            st.button("Ver Detalhes do Projeto", key="btn1")

    st.divider()

    # Projeto 2: WhatsApp/Make
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.video("https://www.youtube.com/watch?v=Exemplo2")
        with col2:
            st.subheader("Notificação Leads (Make/WhatsApp)")
            st.write("Fluxo que envia mensagens instantâneas assim que um formulário é preenchido.")
            st.info("Tecnologias: Make.com, Google Sheets API, WhatsApp API.")

# --- ABA: DASHBOARDS ---
elif aba == "Dashboards Interativos":
    st.title("Visualização de Dados")
    st.write("Exemplos de dashboards que criam 'inteligência' a partir de folhas de Excel.")

    # Aqui podes inserir um gráfico real para o cliente "brincar"
    data = pd.DataFrame({'Mes': ['Jan', 'Fev', 'Mar'], 'Vendas': [100, 150, 130]})
    import plotly.express as px

    fig = px.bar(data, x='Mes', y='Vendas', title="Exemplo de Performance")
    st.plotly_chart(fig, use_container_width=True)
