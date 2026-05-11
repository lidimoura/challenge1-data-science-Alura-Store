import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Alura Store - Executive Insights", layout="wide")

# Sidebar com informações
st.sidebar.title("Lídi Moura")
st.sidebar.info("Estrategista de Dados & Arquiteta de Soluções")
st.sidebar.markdown("---")
st.sidebar.write("[Acesse o Código no GitHub](https://github.com/lidimoura/challenge1-data-science-Alura-Store)")

# --- HEADER ---
st.title(" Alura Store: Relatório Executivo de Otimização")
st.markdown("### Da Análise Exploratória à Decisão de Negócio")

# --- RESUMO EXECUTIVO ---
st.header("Recomendação Estratégica")
st.error("**Ação Sugerida: Fechamento da Unidade Operacional Loja 4**")
st.write("""
    A análise identificou que a **Loja 4** é o principal gargalo da rede. 
    Embora tenha o frete mais baixo, ela não converte volume em lucro, operando consistentemente abaixo da média.
""")

# Carregar Dados
@st.cache_data
def load_data():
    return pd.read_csv("AluraStoreBrasil.csv")

df = load_data()

# --- DASHBOARD ---
tab1, tab2 = st.tabs(["Análise de Faturamento", "Eficiência por Loja"])

with tab1:
    st.subheader("Faturamento Total por Unidade")
    fig, ax = plt.subplots(figsize=(10, 4))
    faturamento = df.groupby('Loja')['Preço'].sum().reset_index()
    sns.barplot(data=faturamento, x='Loja', y='Preço', palette='viridis', ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader("Média de Vendas (Ticket Médio)")
    fig, ax = plt.subplots(figsize=(10, 4))
    media_vendas = df.groupby('Loja')['Preço'].mean().reset_index()
    sns.barplot(data=media_vendas, x='Loja', y='Preço', palette='magma', ax=ax)
    ax.set_xlabel("Unidades (Loja)")
    ax.set_ylabel("Faturamento Médio (R$)")
    st.pyplot(fig)
    st.info("Nota: A Loja 4 apresenta o menor ticket médio, confirmando a ineficiência de vendas.")

# --- RODAPÉ DE TRANSPARÊNCIA ---
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 13px;'>
        <b>Transparência e Vibe Coding:</b> Análise, lógica e estratégia por Lidi Moura. 
        Formatação e polimento estrutural otimizados com IA (Gemini).<br>
        <i>Tecnologia com propósito. 2024.</i>
    </div>
""", unsafe_allow_html=True)
