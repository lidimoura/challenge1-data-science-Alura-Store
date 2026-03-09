# Alura Store - Data Analytics & Insights Strategist

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-CONCLU%C3%8DDO-green?style=for-the-badge)

## Visão Geral do Projeto
Este projeto de análise exploratória de dados (EDA) foi desenvolvido para dar suporte à tomada de decisão executiva da rede Alura Store. O objetivo central foi processar a base de vendas, identificar padrões de consumo, avaliar custos logísticos e, por fim, recomendar estrategicamente o fechamento da unidade menos rentável da rede.

## Stack Tecnológica
- **Python & Pandas**: Limpeza de dados nulos, manipulação de DataFrames e cálculo de KPIs (faturamento, ticket médio, rentabilidade).
- **Matplotlib & Seaborn**: Geração de visualizações estatísticas para Data Storytelling.
- **Google Colab**: Ambiente de prototipagem e documentação técnica.

## Resultados e Recomendação Estratégica
A análise verificou métricas de satisfação, desempenho de vendas por categoria (Eletrônicos, Móveis, Brinquedos) e eficiência logística. O insight principal apontou a **loja 4** como o gargalo operacional de toda a rede. 

Apesar de ter o frete médio mais baixo, a unidade falhou em converter essa vantagem em lucratividade, inclusive nas categorias de alta demanda. A decisão técnica pelo fechamento da loja 4 é sustentada principalmente por dois indicadores críticos visualizados no projeto:

1. **Lucro Mensal Médio Anual**: Demonstra a consistência do baixo desempenho financeiro da Loja 4 em comparação com as filiais concorrentes.
2. **Receita Média por Venda**: Comprova a ineficiência de conversão e o ticket médio muito abaixo do ponto de equilíbrio ideal.

![Receita Média por Loja](receita_media_loja4.png)

![Receita Média por Loja](img/receita_media_loja4.png)

<p align="center">
  <img src="img/receita_media_por_loja.png" alt="Gráfico de Receita Média" width="600">
</p>

## Como Explorar a Análise
1. Clone este repositório.
2. Abra o arquivo `.ipynb` no [Google Colab](https://colab.research.google.com/).
3. Certifique-se de fazer o upload do dataset `AluraStoreBrasil.csv` no ambiente.
4. Execute as células para acompanhar a linha de raciocínio lógico e a geração dos gráficos.
