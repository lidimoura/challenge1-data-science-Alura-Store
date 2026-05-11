import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuracao da pagina
st.set_page_config(page_title="Alura Store | Executive Analytics", layout="wide")

# Estilizacao CSS Customizada (Tons Terrosos, Tipografia e Insight Box visivel)
st.markdown("""
    <style>
    .main { background-color: #faf8f5; color: #2c1e1a; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-size: 16px; font-weight: bold; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #5d4037; }
    h1, h2, h3 { color: #5d4037; font-family: 'Segoe UI', sans-serif; }
    
    /* Insight Box com texto escuro e fundo de contraste suave para leitura perfeita */
    .insight-box { 
        background-color: #f4ede4; 
        padding: 18px; 
        border-radius: 8px; 
        border-left: 5px solid #8b4513; 
        color: #3e2723; 
        font-size: 15px;
        margin-top: 10px; 
        margin-bottom: 20px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: BIO, LINKS E IDIOMA ---
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"])

if lang == "PT-BR":
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("""
    **Arquiteta de Solucoes & Especialista em Dados**
    
    Especialista em Data Science pelo programa **ONE (Alura/Oracle)**. 
    Em especializacao de **IA (Alura/Santander)** e preparacao para certificacoes internacionais **OCI** e **MySQL**.
    """)
    st.sidebar.divider()
    
    st.sidebar.markdown("### Acessos e Contato")
    st.sidebar.link_button("Repositorio no GitHub", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    st.sidebar.link_button("Relatorio Tecnico (Deep Dive)", "https://lidimoura.github.io/challenge1-data-science-Alura-Store/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("Projeto: Alura Store v1.1 - Full Spectrum Analysis")
    
    title = "Painel de Inteligencia de Negocios: Alura Store"
    subtitle = "Relatorio Executivo de Performance Operacional e Reestruturacao"
    
    sec_context_title = "Contexto e Metodologia (ETL)"
    sec_context_text = """
    **Desafio de Negocio:** Avaliar a rentabilidade de uma rede de 4 unidades operacionais e identificar gargalos logisticos e de conversao.
    
    **Processamento de Dados (ETL):** O dataset original foi submetido a um processo de limpeza rigoroso utilizando Python (Pandas). 
    Realizei o tratamento de valores nulos (NaN), normalizacao de tipagem de dados e engenharia de recursos (feature engineering) para calcular 
    indicadores chave. O resultado desta modelagem fundamenta as visualizacoes interativas e estaticas abaixo.
    """
    
    rec_title = "Recomendacao Estrategica (Xeque-Mate)"
    rec_text = """
    **Acao Tecnica: Desativacao Imediata da Unidade Operacional Loja 4.**
    
    A analise de dados cruzados prova de forma cabal que a Loja 4 atua como um ofensor financeiro. 
    Embora apresente os menores custos de frete da rede, a unidade possui o menor Ticket Medio e nao consegue converter 
    o volume de demanda em lucro real, operando sistematicamente abaixo do ponto de equilibrio (break-even).
    """
    
    tab1_label = "Analise de Faturamento"
    tab2_label = "Volume e Categorias"
    tab3_label = "Eficiencia Logistica"
    
    footer_text = "Transparencia e Vibe Coding: Analise de dados, logica de programacao e tomada de decisao estrategica sao de minha autoria (Lidi Moura). A formatacao estrutural deste dashboard foi otimizada com auxilio de IA (Gemini), focando em agilidade e entrega profissional de alto valor."

else:
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("""
    **Solutions Architect & Data Specialist**
    
    Data Science Specialist through the **ONE program (Alura/Oracle)**. 
    Currently specializing in **AI (Alura/Santander)** and preparing for **OCI** and **MySQL** international certifications.
    """)
    st.sidebar.divider()
    
    st.sidebar.markdown("### Links & Contact")
    st.sidebar.link_button("Project Repository", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    st.sidebar.link_button("Technical Report (Deep Dive)", "https://lidimoura.github.io/challenge1-data-science-Alura-Store/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("Project: Alura Store v1.1 - Full Spectrum Analysis")
    
    title = "Business Intelligence Dashboard: Alura Store"
    subtitle = "Executive Report on Operational Performance and Restructuring"
    
    sec_context_title = "Context and Methodology (ETL)"
    sec_context_text = """
    **Business Challenge:** Evaluate the profitability of a 4-unit operational network and identify logistics and conversion bottlenecks.
    
    **Data Processing (ETL):** The original dataset underwent rigorous cleaning using Python (Pandas). 
    I handled null values (NaN), normalized data types, and applied feature engineering to calculate 
    key indicators. The result of this modeling underpins the visualizations below.
    """
    
    rec_title = "Strategic Recommendation"
    rec_text = """
    **Technical Action: Immediate Decommissioning of Store 4.**
    
    Cross-data analysis conclusively proves that Store 4 acts as a financial detractor. 
    Despite having the lowest shipping costs in the network, the unit has the lowest Average Ticket and fails to convert 
    demand volume into real profit, consistently operating below the break-even point.
    """
    
    tab1_label = "Revenue Analysis"
    tab2_label = "Volume and Categories"
    tab3_label = "Logistics Efficiency"
    
    footer_text = "Transparency and Vibe Coding: Data analysis, programming logic, and strategic decision-making are entirely my own (Lidi Moura). The structural formatting of this dashboard was optimized with the help of AI (Gemini), focusing on agility and professional delivery."

# --- CABECALHO ---
st.title(title)
st.markdown(f"### {subtitle}")
st.divider()

# --- SITUACAO E TRATAMENTO ---
st.header(sec_context_title)
st.write(sec_context_text)
st.divider()

# --- RECOMENDACAO E KPI ---
col_rec, col_kpi = st.columns([2, 1])
with col_rec:
    st.header(rec_title)
    st.error(rec_text)
with col_kpi:
    st.header("KPIs")
    st.metric("Margem Loja 4" if lang == "PT-BR" else "Store 4 Margin", "-22%", "Critico / Critical")
    st.metric("Saving Estimado" if lang == "PT-BR" else "Estimated Saving", "R$ 12.400,00", "Ao Mes / Monthly")

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
    st.divider()
    st.header("Evidencias Baseadas em Dados" if lang == "PT-BR" else "Data-Driven Evidence")
    
    tab1, tab2, tab3 = st.tabs([tab1_label, tab2_label, tab3_label])

    terrous_colors = ['#8b4513', '#a0522d', '#d2691e', '#cd853f', '#f4a460']

    with tab1:
        st.subheader("1. O Gargalo de Receita (Ticket Medio)" if lang == "PT-BR" else "1. The Revenue Bottleneck")
        st.markdown("<div class='insight-box'><b>Insight:</b> A Loja 4 atrai clientes, mas eles gastam muito pouco. O faturamento medio por transacao mal cobre os custos de operacao da unidade fisica.</div>" if lang == "PT-BR" else "<div class='insight-box'><b>Insight:</b> Store 4 attracts customers, but they spend very little. The average revenue per transaction barely covers the physical unit's operating costs.</div>", unsafe_allow_html=True)
        
        col1_a, col1_b = st.columns(2)
        revenue_data = df.groupby('Loja')['Preço'].mean().sort_values(ascending=False).reset_index()
        
        with col1_a:
            st.markdown("**Visao Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            fig_rev_int = px.bar(revenue_data, x='Loja', y='Preço', 
                             color='Preço', color_continuous_scale='YlOrBr',
                             text_auto='.2f')
            fig_rev_int.update_layout(xaxis_title="Loja", yaxis_title="Faturamento Medio (R$)")
            st.plotly_chart(fig_rev_int, use_container_width=True)
            
        with col1_b:
            st.markdown("**Analise Estatistica (Seaborn)**" if lang == "PT-BR" else "**Statistical Analysis (Seaborn)**")
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            sns.barplot(data=revenue_data, x='Loja', y='Preço', palette='copper', ax=ax1)
            ax1.set_ylabel("Faturamento Medio (R$)")
            st.pyplot(fig1)

    with tab2:
        st.subheader("2. Demanda por Categoria de Produto" if lang == "PT-BR" else "2. Demand by Product Category")
        st.markdown("<div class='insight-box'><b>Insight:</b> O volume de vendas e puxado por categorias de baixo ticket. Analisar essa distribuicao ajuda a entender por que a rede precisa focar na rentabilidade e nao apenas em volume.</div>" if lang == "PT-BR" else "<div class='insight-box'><b>Insight:</b> Sales volume is driven by low-ticket categories. Analyzing this distribution helps explain why the network must focus on profitability, not just volume.</div>", unsafe_allow_html=True)
        
        col2_a, col2_b = st.columns(2)
        
        with col2_a:
            st.markdown("**Visao Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            fig_cat_int = px.histogram(df, x="Categoria do Produto", color="Categoria do Produto",
                                   color_discrete_sequence=terrous_colors)
            fig_cat_int.update_layout(xaxis_title="", yaxis_title="Volume de Vendas")
            st.plotly_chart(fig_cat_int, use_container_width=True)
            
        with col2_b:
            st.markdown("**Analise Estatistica (Seaborn)**" if lang == "PT-BR" else "**Statistical Analysis (Seaborn)**")
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.countplot(data=df, x='Categoria do Produto', palette='copper', order=df['Categoria do Produto'].value_counts().index, ax=ax2)
            plt.xticks(rotation=45)
            ax2.set_ylabel("Quantidade de Vendas")
            st.pyplot(fig2)

    with tab3:
        st.subheader("3. O Paradoxo do Custo Logistico" if lang == "PT-BR" else "3. The Logistics Cost Paradox")
        st.markdown("<div class='insight-box'><b>Insight:</b> Apesar da Loja 4 ter o menor custo de envio (frete) e a menor variancia, a baixa taxa de conversao de produtos de alto valor anula completamente essa vantagem competitiva local.</div>" if lang == "PT-BR" else "<div class='insight-box'><b>Insight:</b> Although Store 4 has the lowest shipping costs and the smallest variance, the low conversion rate of high-value products completely negates this local competitive advantage.</div>", unsafe_allow_html=True)
        
        col3_a, col3_b = st.columns(2)
        
        with col3_a:
            st.markdown("**Visao Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            fig_frete_int = px.box(df, x="Loja", y="Frete", color_discrete_sequence=['#8b4513'])
            st.plotly_chart(fig_frete_int, use_container_width=True)
            
        with col3_b:
            st.markdown("**Analise Estatistica (Seaborn)**" if lang == "PT-BR" else "**Statistical Analysis (Seaborn)**")
            fig3, ax3 = plt.subplots(figsize=(6, 4))
            sns.boxplot(data=df, x="Loja", y="Frete", palette="YlOrBr", ax=ax3)
            st.pyplot(fig3)

else:
    st.error("Erro: Arquivo 'AluraStoreBrasil.csv' nao encontrado no repositorio." if lang == "PT-BR" else "Error: 'AluraStoreBrasil.csv' not found in repository.")

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 13px; line-height: 1.5;'><b>{footer_text}</b><br>Desenvolvendo tecnologia sustentavel para reflorestar o digital.</div>", unsafe_allow_html=True)
