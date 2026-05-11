import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuracao da pagina
st.set_page_config(page_title="Alura Store | Executive Analytics", layout="wide")

# Estilizacao CSS Customizada (Tons Terrosos e Tipografia Executiva)
st.markdown("""
    <style>
    .main { background-color: #faf8f5; color: #2c1e1a; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-size: 16px; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #5d4037; }
    h1, h2, h3 { color: #5d4037; font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SELETOR DE IDIOMA E PERFIL ---
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"])

if lang == "PT-BR":
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("**Arquiteta de Soluções e Especialista em Dados**")
    st.sidebar.divider()
    
    st.sidebar.markdown("### Portfolio e Contato")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("Projeto: Alura Store v1.0")
    
    title = "Painel de Inteligencia de Negocios: Alura Store"
    subtitle = "Relatorio Executivo de Otimizacao Operacional e Financeira"
    rec_title = "Recomendacao Estrategica"
    rec_text = """
        **Acao Sugerida: Desativacao da Unidade Operacional Loja 4**
        
        A analise identificou que a Loja 4 atua como o principal gargalo de rentabilidade da rede. 
        Embora apresente custos logisticos competitivos, a unidade falha na conversao de faturamento, 
        operando abaixo do ponto de equilibrio (break-even).
    """
    metric_1_label = "Eficiencia Loja 4"
    metric_2_label = "Economia Mensal Estimada"
    tab1_label = "Visao de Mercado"
    tab2_label = "Eficiencia Logistica"
    tab3_label = "Diagnostico de Gargalo"
    footer_text = "Transparencia e Vibe Coding: Analise e estrategia por Lidi Moura. Polimento estrutural otimizado com IA."
    error_msg = "Base de dados nao encontrada. Certifique-se de que o arquivo 'AluraStoreBrasil.csv' esta no seu repositorio GitHub."
else:
    st.sidebar.title("Lidi Moura")
    st.sidebar.markdown("**Solutions Architect and Data Specialist**")
    st.sidebar.divider()

    st.sidebar.markdown("### Portfolio and Networking")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub", "https://github.com/lidimoura")

    st.sidebar.divider()
    st.sidebar.info("Project: Alura Store v1.0")

    title = "Business Intelligence Dashboard: Alura Store"
    subtitle = "Executive Report on Operational and Financial Optimization"
    rec_title = "Strategic Recommendation"
    rec_text = """
        **Suggested Action: Decommissioning of Operational Unit Store 4**
        
        The analysis identified Store 4 as the network's primary profitability bottleneck. 
        Despite competitive logistics costs, the unit fails in revenue conversion, 
        operating below the break-even point.
    """
    metric_1_label = "Store 4 Efficiency"
    metric_2_label = "Estimated Monthly Savings"
    tab1_label = "Market Overview"
    tab2_label = "Logistics Efficiency"
    tab3_label = "Bottleneck Diagnosis"
    footer_text = "Transparency and Vibe Coding: Analysis and strategy by Lidi Moura. Structural polishing optimized with AI."
    error_msg = "Database not found. Please ensure 'AluraStoreBrasil.csv' is present in your GitHub repository."

# --- CABECALHO ---
st.title(title)
st.markdown(f"### {subtitle}")
st.divider()

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
    # --- RESUMO EXECUTIVO ---
    col_rec, col_kpi = st.columns([1.5, 1])

    with col_rec:
        st.header(rec_title)
        st.error(rec_text)

    with col_kpi:
        st.header("KPIs")
        st.metric(metric_1_label, "-22%", "Below Average")
        st.metric(metric_2_label, "R$ 12.400,00", "Projected")

    st.divider()

    # --- ABAS DO RELATORIO ---
    tab1, tab2, tab3 = st.tabs([tab1_label, tab2_label, tab3_label])

    with tab1:
        st.subheader(tab1_label)
        # Paleta de cores manual para evitar erro de atributo
        terrous_colors = ['#8b4513', '#a0522d', '#d2691e', '#cd853f', '#f4a460']
        fig_cat = px.histogram(df, x="Categoria do Produto", color="Categoria do Produto",
                               title="Volume Total de Vendas por Categoria",
                               color_discrete_sequence=terrous_colors)
        st.plotly_chart(fig_cat, use_container_width=True)

    with tab2:
        st.subheader(tab2_label)
        fig_frete = px.box(df, x="Loja", y="Frete", 
                           title="Distribuicao de Custos de Frete por Unidade",
                           color_discrete_sequence=['#8b4513'])
        st.plotly_chart(fig_frete, use_container_width=True)

    with tab3:
        st.subheader(tab3_label)
        revenue_data = df.groupby('Loja')['Preço'].mean().reset_index()
        fig_rev = px.bar(revenue_data, x='Loja', y='Preço', 
                         title="Ticket Medio (Faturamento por Venda) por Loja",
                         color='Preço', color_continuous_scale='Brwnyl',
                         text_auto='.2f')
        st.plotly_chart(fig_rev, use_container_width=True)
else:
    st.error(error_msg)

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 14px;'>{footer_text}</div>", unsafe_allow_html=True)
