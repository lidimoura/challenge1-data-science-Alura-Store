import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuracao da pagina
st.set_page_config(page_title="Alura Store | Executive Analytics", layout="wide")

# Estilizacao para tons terrosos e fontes limpas
st.markdown("""
    <style>
    .main { background-color: #faf8f5; color: #2c1e1a; }
    h1, h2, h3 { color: #5d4037; font-family: 'Segoe UI', sans-serif; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #8b4513; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: IDIOMA, REPO E CONTATO ---
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"])

if lang == "PT-BR":
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("**Arquiteta de Soluções e Especialista em Dados**")
    st.sidebar.divider()
    
    st.sidebar.markdown("### Acesso ao Projeto")
    st.sidebar.link_button("Repositório no GitHub", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    
    st.sidebar.markdown("### Contato Profissional")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("Versão do App: 1.1.0")
    
    title = "Painel de Inteligência de Negócios: Alura Store"
    subtitle = "Análise de Performance Operacional e Decisão Estratégica"
    
    sec_context_title = "Situação e Metodologia"
    sec_context_text = """
    **Desafio:** Identificar ineficiências em uma rede de 4 unidades e otimizar a lucratividade global.
    
    **Tratamento de Dados (ETL):** Os dados brutos passaram por um processo rigoroso de limpeza de valores nulos, 
    ajuste de tipagem (casting) e normalização de categorias. Utilizei Python e Pandas para calcular KPIs de 
    faturamento real, ticket médio e impacto do custo logístico (frete) sobre a margem de cada loja.
    """
    
    rec_title = "Recomendação Executiva"
    rec_text = """
    **Ação Técnica: Desativação da Loja 4.**
    
    A Unidade 4 apresenta o menor faturamento médio por venda da rede. Apesar de custos de frete reduzidos, 
    a conversão em lucro é insuficiente para sustentar a operação, tornando-a o principal gargalo financeiro.
    """
    
    tab1_label = "Faturamento por Unidade"
    tab2_label = "Volume por Categoria"
    footer_text = "Transparência e Vibe Coding: Análise e estratégia por Lidi Moura. Polimento estrutural otimizado com IA."

else:
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("**Solutions Architect and Data Specialist**")
    st.sidebar.divider()
    
    st.sidebar.markdown("### Project Access")
    st.sidebar.link_button("GitHub Repository", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    
    st.sidebar.markdown("### Professional Contact")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("App Version: 1.1.0")

    title = "Business Intelligence Dashboard: Alura Store"
    subtitle = "Operational Performance Analysis and Strategic Decision"
    
    sec_context_title = "Situation and Methodology"
    sec_context_text = """
    **Challenge:** Identify inefficiencies across 4 units and optimize overall network profitability.
    
    **Data Processing (ETL):** Raw data underwent a rigorous process of null value handling, type casting, 
    and category normalization. I used Python and Pandas to calculate KPIs for actual revenue, average ticket, 
    and the impact of logistics costs (freight) on each store's margin.
    """
    
    rec_title = "Executive Recommendation"
    rec_text = """
    **Technical Action: Decommissioning of Store 4.**
    
    Unit 4 shows the network's lowest average revenue per sale. Despite lower shipping costs, the conversion 
    into profit is insufficient to sustain the operation, making it the primary financial bottleneck.
    """
    
    tab1_label = "Revenue per Unit"
    tab2_label = "Volume per Category"
    footer_text = "Transparency and Vibe Coding: Analysis and strategy by Lidi Moura. Structural polishing optimized with AI."

# --- CABECALHO ---
st.title(title)
st.markdown(f"### {subtitle}")
st.divider()

# --- SITUACAO E TRATAMENTO ---
st.header(sec_context_title)
st.write(sec_context_text)

# --- RECOMENDACAO ---
st.divider()
st.header(rec_title)
st.error(rec_text)

# --- CARREGAMENTO DE DADOS ---
@st.cache_data
def load_data():
    file_path = "AluraStoreBrasil.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path).dropna()
    else:
        return None

df = load_data()

if df is not None:
    # --- ANALISE VISUAL (MATPLOTLIB/SEABORN) ---
    st.divider()
    tab1, tab2 = st.tabs([tab1_label, tab2_label])

    with tab1:
        st.subheader(tab1_label)
        # Recriando o grafico do ticket medio (faturamento medio)
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        revenue_data = df.groupby('Loja')['Preço'].mean().sort_values(ascending=False).reset_index()
        sns.barplot(data=revenue_data, x='Loja', y='Preço', palette='copper', ax=ax1)
        ax1.set_ylabel("Faturamento Médio (R$)" if lang == "PT-BR" else "Average Revenue (R$)")
        ax1.set_xlabel("Unidade (Loja)" if lang == "PT-BR" else "Unit (Store)")
        st.pyplot(fig1)

    with tab2:
        st.subheader(tab2_label)
        # Recriando o grafico de volume por categoria
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        sns.countplot(data=df, x='Categoria do Produto', palette='copper', order=df['Categoria do Produto'].value_counts().index, ax=ax2)
        plt.xticks(rotation=45)
        ax2.set_ylabel("Quantidade de Vendas" if lang == "PT-BR" else "Sales Quantity")
        st.pyplot(fig2)
else:
    st.error("Erro: Arquivo 'AluraStoreBrasil.csv' não encontrado no repositório." if lang == "PT-BR" else "Error: 'AluraStoreBrasil.csv' not found in repository.")

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 14px;'>{footer_text}</div>", unsafe_allow_html=True)
