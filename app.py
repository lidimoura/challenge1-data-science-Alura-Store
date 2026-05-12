import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuracao da pagina
st.set_page_config(page_title="Alura Store | Executive Analytics", layout="wide")

# Estilizacao CSS (Insight Box com texto escuro e tons terrosos, estritamente sem emojis)
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
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: BIO, LINKS E IDIOMA ---
lang = st.sidebar.selectbox("Language / Idioma", ["PT-BR", "EN"])

if lang == "PT-BR":
    st.sidebar.title("Lídi Moura")
    st.sidebar.markdown("""
    **Arquiteta de Soluções e Especialista em Dados**
    
    Especialista em Data Science pelo programa **ONE (Alura/Oracle)**. 
    Em especializacao de **IA (Alura/Santander)** e preparacao para certificacoes internacionais **OCI** e **MySQL**.
    """)
    st.sidebar.divider()
    
    st.sidebar.markdown("### Acessos e Contato")
    st.sidebar.link_button("Repositório no GitHub", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    st.sidebar.link_button("Relatório Tecnico (Deep Dive)", "https://lidimoura.github.io/challenge1-data-science-Alura-Store/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("Projeto: Alura Store v2.0 - Full Spectrum Analysis")
    
    title = "Painel de Inteligência de Negócios: Alura Store"
    subtitle = "Relatório Executivo de Performance Operacional e Reestruturação"
    
    sec_context_title = "Contexto e Metodologia (ETL)"
    sec_context_text = """
    **Desafio de Negocio:** Avaliar a rentabilidade de uma rede de 4 unidades operacionais e identificar gargalos logísticos e de conversão.
    
    **Processamento de Dados (ETL):** O dataset original foi submetido a um processo de limpeza rigoroso utilizando Python (Pandas). 
    Realizei o tratamento de valores nulos (NaN), normalização de tipagem de dados e engenharia de recursos (feature engineering) para calcular 
    indicadores chave como Ticket Médio, Lucratividade Mensal, Volume de Vendas por Categoria e Impacto do Frete. O resultado desta modelagem fundamenta as visualizacoes interativas e estaticas abaixo, demonstrando proficiencia na aplicaço de múltiplas bibliotecas visuais (Plotly, Seaborn, Matplotlib).
    """
    
    rec_title = "Recomendaço Estratégica (Xeque-Mate)"
    rec_text = """
    **Ação Técnica: Desativação Imediata da Unidade Operacional Loja 4.**
    
    A análise de dados cruzados prova de forma cabal que a Loja 4 atua como um ofensor financeiro. 
    Embora apresente os menores custos de frete da rede, a unidade possui o menor Ticket Medio e nao consegue converter 
    o volume de demanda em lucro real, operando sistematicamente abaixo do ponto de equilibrio ideal da rede.
    """
    
    tab1_label = "Lucro Mensal Médio"
    tab2_label = "Receita Média por Venda"
    tab3_label = "Faturamento Total"
    tab4_label = "Volume e Categorias"
    tab5_label = "Eficiencia Logistica"
    
    footer_text = "Transparência e Vibe Coding: Análise de dados, lógica de programação e tomada de decisão estratégica são de minha autoria (Lídi Moura). A formatação estrutural deste dashboard foi otimizada com auxílio de IA, focando em agilidade e entrega profissional de alto valor."

else:
    st.sidebar.title("Lídi Moura")
    st.sidebar.markdown("""
    **Solutions Architect and Data Specialist**
    
    Data Science Specialist through the **ONE program (Alura/Oracle)**. 
    Currently specializing in **AI (Alura/Santander)** and preparing for **OCI** and **MySQL** international certifications.
    """)
    st.sidebar.divider()
    
    st.sidebar.markdown("### Links and Contact")
    st.sidebar.link_button("Project Repository", "https://github.com/lidimoura/challenge1-data-science-Alura-Store")
    st.sidebar.link_button("Technical Report (Deep Dive)", "https://lidimoura.github.io/challenge1-data-science-Alura-Store/")
    st.sidebar.link_button("LinkedIn", "https://linkedin.com/in/lidimoura")
    st.sidebar.link_button("GitHub Profile", "https://github.com/lidimoura")
    
    st.sidebar.divider()
    st.sidebar.info("Project: Alura Store v2.0 - Full Spectrum Analysis")
    
    title = "Business Intelligence Dashboard: Alura Store"
    subtitle = "Executive Report on Operational Performance and Restructuring"
    
    sec_context_title = "Context and Methodology (ETL)"
    sec_context_text = """
    **Business Challenge:** Evaluate the profitability of a 4-unit operational network and identify logistics and conversion bottlenecks.
    
    **Data Processing (ETL):** The raw dataset underwent rigorous cleaning using Python (Pandas). 
    I handled null values (NaN), normalized data types, and applied feature engineering to calculate 
    key indicators such as Average Ticket, Monthly Profitability, Sales Volume by Category, and Freight Impact. This modeling underpins the interactive and static visualizations below, demonstrating proficiency across multiple visual libraries (Plotly, Seaborn, Matplotlib).
    """
    
    rec_title = "Strategic Recommendation"
    rec_text = """
    **Technical Action: Immediate Decommissioning of Store 4.**
    
    Cross-data analysis conclusively proves that Store 4 acts as a financial detractor. 
    Despite having the lowest shipping costs in the network, the unit has the lowest Average Ticket and fails to convert 
    demand volume into real profit, consistently operating below the network's ideal break-even point.
    """
    
    tab1_label = "Average Monthly Profit"
    tab2_label = "Average Revenue per Sale"
    tab3_label = "Total Revenue"
    tab4_label = "Volume and Categories"
    tab5_label = "Logistics Efficiency"
    
    footer_text = "Transparency and Vibe Coding: Data analysis, programming logic, and strategic decision-making are entirely my own (Lidi Moura). The structural formatting of this dashboard was optimized with AI assistance, focusing on agility and professional delivery."

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
    st.header("EvidÊncias Baseadas em Dados (Full Spectrum)" if lang == "PT-BR" else "Data-Driven Evidence (Full Spectrum)")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([tab1_label, tab2_label, tab3_label, tab4_label, tab5_label])
    terrous_colors = ['#8b4513', '#a0522d', '#d2691e', '#cd853f', '#f4a460']

    # ABA 1: Lucro Mensal (Foco README)
    with tab1:
        st.subheader(tab1_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'O grafico abaixo demonstra a consistencia do baixo desempenho financeiro da loja 4 em comparacao com as filiais concorrentes ao longo dos meses. Esta visualizacao justifica a necessidade imediata de contencao de gastos operacionais nesta unidade.' if lang == 'PT-BR' else 'The chart below demonstrates the consistency of store 4 low financial performance compared to competing branches over the months. This visualization justifies the immediate need to contain operating costs at this unit.'}</div>", unsafe_allow_html=True)
        col1_a, col1_b = st.columns(2)
        with col1_a:
            st.markdown("**Visão Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            if 'Data' in df.columns:
                df_temp = df.copy()
                df_temp['Data'] = pd.to_datetime(df_temp['Data'])
                df_temp['Mes'] = df_temp['Data'].dt.month
                lucro_data = df_temp.groupby(['Mes', 'Loja'])['Preço'].sum().reset_index()
                fig1_int = px.line(lucro_data, x='Mes', y='Preço', color='Loja', color_discrete_sequence=terrous_colors)
            else:
                lucro_data = df.groupby('Loja')['Preço'].sum().reset_index()
                fig1_int = px.bar(lucro_data, x='Loja', y='Preço', color='Loja', color_discrete_sequence=terrous_colors)
            st.plotly_chart(fig1_int, use_container_width=True)
            
        with col1_b:
            st.markdown("**Documentação Técnica (Ref. README)**" if lang == "PT-BR" else "**Technical Documentation (README Ref.)**")
            if os.path.exists("assets/grafico_lucro_mensal_medio_anual.png"):
                st.image("assets/grafico_lucro_mensal_medio_anual.png", use_container_width=True)
            else:
                st.info("Imagem 'grafico_lucro_mensal_medio_anual.png' documentada no relatorio base." if lang == "PT-BR" else "Image documented in base report.")

    # ABA 2: Receita Media por Venda (Foco README)
    with tab2:
        st.subheader(tab2_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Aqui, comprovamos a ineficiencia de conversao. O ticket medio da loja 4 opera muito abaixo do ponto de equilibrio ideal da rede, comprovando que volume de vendas local nao se traduz em lucratividade real.' if lang == 'PT-BR' else 'Here, we prove the conversion inefficiency. Store 4 average ticket operates well below the ideal break-even point, proving that local sales volume does not translate into real profitability.'}</div>", unsafe_allow_html=True)
        col2_a, col2_b = st.columns(2)
        with col2_a:
            st.markdown("**Visão Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            rev_data = df.groupby('Loja')['Preço'].mean().reset_index()
            fig2_int = px.bar(rev_data, x='Loja', y='Preço', color='Preço', color_continuous_scale='YlOrBr', text_auto='.2f')
            fig2_int.update_layout(xaxis_title="Loja", yaxis_title="Faturamento Medio (R$)")
            st.plotly_chart(fig2_int, use_container_width=True)
            
        with col2_b:
            st.markdown("**Documentação Técnica (Ref. README)**" if lang == "PT-BR" else "**Technical Documentation (README Ref.)**")
            if os.path.exists("assets/grafico_receita_media_por_loja.png"):
                st.image("assets/grafico_receita_media_por_loja.png", use_container_width=True)
            else:
                st.info("Imagem 'grafico_receita_media_venda.png' documentada no relatorio base." if lang == "PT-BR" else "Image documented in base report.")

    # ABA 3: Faturamento Total por Unidade
    with tab3:
        st.subheader(tab3_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'Analise consolidada da receita bruta gerada por cada filial. A Loja 4 contribui de forma limitante para a receita global da rede, reforcando a hipotese de reestruturacao.' if lang == 'PT-BR' else 'Consolidated analysis of gross revenue generated by each branch. Store 4 contributes marginally to the global revenue, reinforcing the restructuring hypothesis.'}</div>", unsafe_allow_html=True)
        col3_a, col3_b = st.columns(2)
        
        fat_data = df.groupby('Loja')['Preço'].sum().reset_index()
        with col3_a:
            st.markdown("**Visao Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            fig3_int = px.bar(fat_data, x='Loja', y='Preço', color='Loja', color_discrete_sequence=terrous_colors, text_auto='.2s')
            fig3_int.update_layout(xaxis_title="Loja", yaxis_title="Faturamento Total (R$)")
            st.plotly_chart(fig3_int, use_container_width=True)
        with col3_b:
            st.markdown("**Análise Estatística (Seaborn)**" if lang == "PT-BR" else "**Statistical Analysis (Seaborn)**")
            fig3_stat, ax3 = plt.subplots(figsize=(6, 4))
            sns.barplot(data=fat_data, x='Loja', y='Preço', palette='copper', ax=ax3)
            ax3.set_ylabel("Faturamento Total (R$)")
            st.pyplot(fig3_stat)

    # ABA 4: Volume de Vendas por Categoria
    with tab4:
        st.subheader(tab4_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'O volume de vendas e puxado por categorias de baixo ticket. Analisar essa distribuicao ajuda a entender a composicao da demanda e por que a rede precisa focar na rentabilidade por produto.' if lang == 'PT-BR' else 'Sales volume is driven by low-ticket categories. Analyzing this distribution helps to understand demand composition and why the network must focus on per-product profitability.'}</div>", unsafe_allow_html=True)
        col4_a, col4_b = st.columns(2)
        with col4_a:
            st.markdown("**Visão Interativa (Plotly)**" if lang == "PT-BR" else "**Interactive View (Plotly)**")
            fig_cat_int = px.histogram(df, x="Categoria do Produto", color="Categoria do Produto", color_discrete_sequence=terrous_colors)
            st.plotly_chart(fig_cat_int, use_container_width=True)
            
        with col4_b:
            st.markdown("**Análise Estatística (Seaborn)**" if lang == "PT-BR" else "**Statistical Analysis (Seaborn)**")
            fig4_stat, ax4 = plt.subplots(figsize=(6, 4))
            sns.countplot(data=df, x='Categoria do Produto', palette='copper', order=df['Categoria do Produto'].value_counts().index, ax=ax4)
            plt.xticks(rotation=45)
            ax4.set_ylabel("Quantidade" if lang == "PT-BR" else "Quantity")
            st.pyplot(fig4_stat)

    # ABA 5: Eficiencia Logistica (Frete)
    with tab5:
        st.subheader(tab5_label)
        st.markdown(f"<div class='insight-box'><b>Insight:</b> {'O Paradoxo do Custo Logistico: Apesar da Loja 4 ter o menor custo de envio (frete) e a menor variancia, a baixa taxa de conversao de produtos de alto valor anula completamente essa vantagem competitiva local.' if lang == 'PT-BR' else 'The Logistics Cost Paradox: Although Store 4 has the lowest shipping costs and smallest variance, the low conversion rate of high-value products negates this competitive advantage.'}</div>", unsafe_allow_html=True)
        col5_a, col5_b = st.columns(2)
        with col5_a:
            st.markdown("**Distribuição Interativa (Plotly Boxplot)**" if lang == "PT-BR" else "**Interactive Distribution (Plotly Boxplot)**")
            fig_frete_int = px.box(df, x="Loja", y="Frete", color_discrete_sequence=['#8b4513'])
            st.plotly_chart(fig_frete_int, use_container_width=True)
            
        with col5_b:
            st.markdown("**Análise Estatística (Seaborn Boxplot)**" if lang == "PT-BR" else "**Statistical Analysis (Seaborn Boxplot)**")
            fig5_stat, ax5 = plt.subplots(figsize=(6, 4))
            sns.boxplot(data=df, x="Loja", y="Frete", palette="YlOrBr", ax=ax5)
            st.pyplot(fig5_stat)

else:
    st.error("Erro: Arquivo 'AluraStoreBrasil.csv' nao encontrado no repositorio." if lang == "PT-BR" else "Error: 'AluraStoreBrasil.csv' not found in repository.")

# --- RODAPE ---
st.divider()
st.markdown(f"<div style='text-align: center; color: #666; font-size: 13px; line-height: 1.5;'><b>{footer_text}</b><br>Desenvolvendo tecnologia sustentavel para reflorestar o digital.</div>", unsafe_allow_html=True)
