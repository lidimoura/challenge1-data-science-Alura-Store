import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuracao da pagina
st.set_page_config(page_title="Alura Store | Executive Analytics", layout="wide")

# Estilizacao CSS (Insight Box com texto escuro e tons terrosos, sem emojis)
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

# --- SIDEBAR: BIO, LINKS E IDIOMA ---
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"])

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
    
    title, subtitle = "Painel: Alura Store", "Relatorio Executivo de Performance"
    sec_context_title = "Contexto e Metodologia (ETL)"
    sec_context_text = "O dataset original foi submetido a limpeza rigorosa com Python (Pandas), tratando valores nulos e normalizando dados para calcular Ticket Medio e Rentabilidade Mensal."
    rec_title, rec_text = "Recomendacao Estrategica", "Acao Tecnica: Desativacao Imediata da Unidade Operacional Loja 4. A unidade opera sistematicamente abaixo do ponto de equilibrio da rede."
    tab1_label, tab2_label = "Lucro Mensal Medio Anual", "Receita Media por Venda"
    footer_text = "Transparencia e Vibe Coding: Analise de dados e estrategia por Lidi Moura. Polimento estrutural otimizado com IA."
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
    
    title, subtitle = "Dashboard: Alura Store", "Executive Performance Report"
    sec_context_title = "Context and Methodology (ETL)"
    sec_context_text = "The raw dataset underwent rigorous cleaning using Python (Pandas), handling null values and normalizing data to calculate Average Ticket and Monthly Profitability."
    rec_title, rec_text = "Strategic Recommendation", "Technical Action: Immediate Decommissioning of Store 4. The unit consistently operates below the network's break-even point."
    tab1_label, tab2_label = "Average Annual Monthly Profit", "Average Revenue per Sale"
    footer_text = "Transparency and Vibe Coding: Data analysis and strategy by Lidi Moura. Structural polishing optimized with AI."

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

# --- CARREGAMENTO ---
@st.cache_data
def load_data():
    if os.path.exists("AluraStoreBrasil.csv"):
        return pd.read_csv("AluraStoreBrasil.csv").dropna()
    return None

df = load_data()

if df is not None:
    st.divider()
    # Apenas as duas abas que estao no seu README
    tab1, tab2 = st.tabs([tab1_label, tab2_label])

    # ABA 1: Lucro Mensal Medio Anual
    with tab1:
        st.subheader(tab1_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Demonstracao da consistencia do baixo desempenho financeiro da loja 4 em comparacao com as filiais concorrentes ao longo dos meses.' if lang == 'PT-BR' else 'Demonstrates the consistent underperformance of store 4 compared to competing branches over the months.'}</div>", unsafe_allow_html=True)
        
        col1_a, col1_b = st.columns(2)
        
        with col1_a:
            st.markdown("**Visao Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            # Agrupamento para receita mensal. Se voce usou colunas diferentes, o Plotly se ajusta aqui.
            if 'Data' in df.columns:
                df['Data'] = pd.to_datetime(df['Data'])
                df['Mes'] = df['Data'].dt.month
                lucro_data = df.groupby(['Mes', 'Loja'])['Preço'].sum().reset_index()
                fig1_int = px.line(lucro_data, x='Mes', y='Preço', color='Loja', title="Evolucao Mensal", color_discrete_sequence=['#8b4513', '#a0522d', '#cd853f', '#f4a460'])
                st.plotly_chart(fig1_int, use_container_width=True)
            else:
                # Fallback caso a coluna Data nao exista no CSV bruto (agrupa pelo total para nao quebrar)
                lucro_data = df.groupby('Loja')['Preço'].sum().reset_index()
                fig1_int = px.bar(lucro_data, x='Loja', y='Preço', color='Loja', title="Faturamento Consolidado", color_discrete_sequence=['#8b4513', '#a0522d', '#cd853f', '#f4a460'])
                st.plotly_chart(fig1_int, use_container_width=True)

        with col1_b:
            st.markdown("**Grafico Original (Colab / README)**" if lang == "PT-BR" else "**Original Chart (Colab / README)**")
            # Puxando exatamente a imagem do seu README
            if os.path.exists("assets/grafico_lucro_mensal_medio_anual.png"):
                st.image("assets/grafico_lucro_mensal_medio_anual.png", use_container_width=True)
            else:
                st.warning("Imagem assets/grafico_lucro_mensal_medio_anual.png nao encontrada no repositorio.")

    # ABA 2: Receita Media por Venda
    with tab2:
        st.subheader(tab2_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Aqui, comprovamos a ineficiencia de conversao. O ticket medio da loja 4 opera muito abaixo do ponto de equilibrio ideal da rede.' if lang == 'PT-BR' else 'Here, we prove the conversion inefficiency. Store 4 average ticket operates well below the ideal break-even point.'}</div>", unsafe_allow_html=True)
        
        col2_a, col2_b = st.columns(2)
        
        with col2_a:
            st.markdown("**Visao Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            rev_data = df.groupby('Loja')['Preço'].mean().reset_index()
            fig2_int = px.bar(rev_data, x='Loja', y='Preço', color='Preço', color_continuous_scale='YlOrBr', text_auto='.2f')
            st.plotly_chart(fig2_int, use_container_width=True)
            
        with col2_b:
            st.markdown("**Grafico Original (Colab / README)**" if lang == "PT-BR" else "**Original Chart (Colab / README)**")
            # Puxando exatamente a imagem do seu README
            if os.path.exists("assets/grafico_receita_media_venda.png"):
                st.image("assets/grafico_receita_media_venda.png", use_container_width=True)
            else:
                st.warning("Imagem assets/grafico_receita_media_venda.png nao encontrada no repositorio.")

else:
    st.error("Arquivo AluraStoreBrasil.csv nao encontrado." if lang == "PT-BR" else "File AluraStoreBrasil.csv not found.")

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 13px;'><b>{footer_text}</b><br>Reflorestando o Digital.</div>", unsafe_allow_html=True)
