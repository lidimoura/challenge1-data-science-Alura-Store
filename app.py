import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURACAO ---
st.set_page_config(page_title="Alura Store | Executive Analytics", layout="wide")

# --- CSS ---
st.markdown("""
    <style>
    .main { background-color: #faf8f5; color: #2c1e1a; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-size: 16px; font-weight: bold; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #5d4037; }
    h1, h2, h3 { color: #5d4037; font-family: 'Segoe UI', sans-serif; }
    .insight-box { 
        background-color: #f4ede4; 
        padding: 18px; 
        border-radius: 8px; 
        border-left: 5px solid #8b4513; 
        color: #3e2723; 
        font-size: 15px;
        margin-top: 10px; 
        margin-bottom: 20px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR E IDIOMA ---
# A propriedade 'key' previne o erro de ElementId duplicado
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"], key="lang_selector_unique")

if lang == "PT-BR":
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("""
    **Arquiteta de Solucoes e Especialista em Dados**
    
    Especialista em Data Science pelo programa **ONE (Alura/Oracle)**. 
    Em especializacao de **IA (Alura/Santander)** e preparacao para certificacoes internacionais **OCI** e **MySQL**.
    """)
    st.sidebar.divider()
    st.sidebar.markdown("### Acessos e Contato")
    st.sidebar.link_button("Repositorio no GitHub", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    st.sidebar.link_button("Relatorio Tecnico (Deep Dive)", "https://lidimoura.github.io/challenge1-data-science-Alura-Store/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    title = "Painel: Alura Store"
    subtitle = "Relatorio Executivo de Performance"
    rec_title = "Recomendacao Estrategica"
    rec_text = "Acao Tecnica: Desativacao Imediata da Unidade Operacional Loja 4. A unidade opera sistematicamente abaixo do ponto de equilibrio."
    tab1_label = "1. Receita Media por Venda"
    tab2_label = "2. Faturamento Total (Lucro)"
    tab3_label = "3. Volume por Categoria"
    tab4_label = "4. Eficiencia Logistica"
    footer_text = "Transparencia e Vibe Coding: Analise e estrategia por Lidi Moura. Polimento otimizado com IA."
else:
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("""
    **Solutions Architect and Data Specialist**
    
    Data Science Specialist through the **ONE program (Alura/Oracle)**. 
    Specializing in **AI (Alura/Santander)** and preparing for **OCI** and **MySQL** certifications.
    """)
    st.sidebar.divider()
    st.sidebar.markdown("### Links and Contact")
    st.sidebar.link_button("Project Repository", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    st.sidebar.link_button("Technical Report (Deep Dive)", "https://lidimoura.github.io/challenge1-data-science-Alura-Store/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    title = "Dashboard: Alura Store"
    subtitle = "Executive Performance Report"
    rec_title = "Strategic Recommendation"
    rec_text = "Technical Action: Immediate Decommissioning of Store 4. The unit consistently operates below the break-even point."
    tab1_label = "1. Average Revenue per Sale"
    tab2_label = "2. Total Revenue (Profit)"
    tab3_label = "3. Volume by Category"
    tab4_label = "4. Logistics Efficiency"
    footer_text = "Transparency and Vibe Coding: Analysis and strategy by Lidi Moura. Polishing optimized with AI."

# --- CABECALHO ---
st.title(title)
st.markdown(f"### {subtitle}")
st.divider()

# --- RECOMENDACAO ---
col_rec, col_kpi = st.columns([2, 1])
with col_rec:
    st.header(rec_title)
    st.error(rec_text)
with col_kpi:
    st.header("KPIs")
    st.metric("Margem Loja 4" if lang == "PT-BR" else "Store 4 Margin", "-22%", "Critico")
    st.metric("Saving Estimado" if lang == "PT-BR" else "Estimated Saving", "R$ 12.400,00", "Mensal")

# --- CARREGAMENTO DE DADOS ---
@st.cache_data
def load_data():
    if os.path.exists("AluraStoreBrasil.csv"):
        return pd.read_csv("AluraStoreBrasil.csv").dropna()
    return None

df = load_data()

if df is not None:
    st.divider()
    # Adicionamos 4 abas para acomodar todos os graficos
    tab1, tab2, tab3, tab4 = st.tabs([tab1_label, tab2_label, tab3_label, tab4_label])

    terrous_colors = ['#8b4513', '#a0522d', '#d2691e', '#cd853f', '#f4a460']

    # --- ABA 1: RECEITA MEDIA POR VENDA (GRAFICO 2 DO README) ---
    with tab1:
        st.subheader(tab1_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'O ticket medio da Loja 4 nao atinge o patamar de rentabilidade ideal da rede.' if lang == 'PT-BR' else 'Store 4 average ticket fails to meet the network profitability standards.'}</div>", unsafe_allow_html=True)
        
        rev_data = df.groupby('Loja')['Preço'].mean().reset_index()
        col1_a, col1_b = st.columns(2)
        
        with col1_a:
            fig1_int = px.bar(rev_data, x='Loja', y='Preço', color='Preço', color_continuous_scale='YlOrBr', text_auto='.2f', title="Plotly (Interativo)")
            st.plotly_chart(fig1_int, use_container_width=True)
        with col1_b:
            fig1_stat, ax1 = plt.subplots(figsize=(6, 4))
            sns.barplot(data=rev_data, x='Loja', y='Preço', palette='copper', ax=ax1)
            ax1.set_title("Seaborn / Matplotlib (Estatico)")
            ax1.set_ylabel("Receita Media (R$)")
            st.pyplot(fig1_stat)

    # --- ABA 2: FATURAMENTO TOTAL / LUCRO (GRAFICO 1 DO README) ---
    with tab2:
        st.subheader(tab2_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'A Loja 4 apresenta o desempenho financeiro mais baixo de forma consistente.' if lang == 'PT-BR' else 'Store 4 consistently shows the lowest total financial performance.'}</div>", unsafe_allow_html=True)
        
        profit_data = df.groupby('Loja')['Preço'].sum().reset_index()
        col2_a, col2_b = st.columns(2)
        
        with col2_a:
            fig2_int = px.bar(profit_data, x='Loja', y='Preço', color='Loja', color_discrete_sequence=terrous_colors, title="Plotly (Interativo)")
            st.plotly_chart(fig2_int, use_container_width=True)
        with col2_b:
            fig2_stat, ax2 = plt.subplots(figsize=(6, 4))
            sns.barplot(data=profit_data, x='Loja', y='Preço', palette='copper', ax=ax2)
            ax2.set_title("Seaborn / Matplotlib (Estatico)")
            ax2.set_ylabel("Faturamento Total (R$)")
            st.pyplot(fig2_stat)

    # --- ABA 3: VOLUME POR CATEGORIA ---
    with tab3:
        st.subheader(tab3_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'A demanda da rede e puxada fortemente por categorias especificas.' if lang == 'PT-BR' else 'Network demand is strongly driven by specific categories.'}</div>", unsafe_allow_html=True)
        
        col3_a, col3_b = st.columns(2)
        with col3_a:
            fig3_int = px.histogram(df, x="Categoria do Produto", color="Categoria do Produto", color_discrete_sequence=terrous_colors, title="Plotly (Interativo)")
            st.plotly_chart(fig3_int, use_container_width=True)
        with col3_b:
            fig3_stat, ax3 = plt.subplots(figsize=(6, 4))
            sns.countplot(data=df, x='Categoria do Produto', palette='copper', order=df['Categoria do Produto'].value_counts().index, ax=ax3)
            plt.xticks(rotation=45)
            ax3.set_title("Seaborn / Matplotlib (Estatico)")
            ax3.set_ylabel("Volume de Vendas")
            st.pyplot(fig3_stat)

    # --- ABA 4: FRETE / LOGISTICA ---
    with tab4:
        st.subheader(tab4_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Apesar da Loja 4 ter o menor custo de envio, ela nao converte isso em vantagem financeira.' if lang == 'PT-BR' else 'Although Store 4 has the lowest shipping cost, it does not convert it into financial advantage.'}</div>", unsafe_allow_html=True)
        
        col4_a, col4_b = st.columns(2)
        with col4_a:
            fig4_int = px.box(df, x="Loja", y="Frete", color_discrete_sequence=['#8b4513'], title="Plotly (Interativo)")
            st.plotly_chart(fig4_int, use_container_width=True)
        with col4_b:
            fig4_stat, ax4 = plt.subplots(figsize=(6, 4))
            sns.boxplot(data=df, x="Loja", y="Frete", palette="YlOrBr", ax=ax4)
            ax4.set_title("Seaborn / Matplotlib (Estatico)")
            st.pyplot(fig4_stat)

else:
    st.error("Arquivo AluraStoreBrasil.csv nao encontrado.")

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 13px;'><b>{footer_text}</b><br>Reflorestando o Digital.</div>", unsafe_allow_html=True)
