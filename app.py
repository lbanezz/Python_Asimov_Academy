# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# Configurando a página do Streamlit para usar o layout em tela cheia (wide)
st.set_page_config(layout="wide")

# Carregando os arquivos CSV com os dados de avaliações e livros
df_reviews = pd.read_csv("datesets/customer reviews.csv")
df_top100_books = pd.read_csv("datesets/Top-100 Trending Books.csv")

# Obtendo o valor máximo e mínimo de preços dos livros
price_max = df_top100_books["book price"].max() 
price_min = df_top100_books["book price"].min()

# Criando um controle deslizante (slider) na barra lateral para filtrar livros por preço
max_price = st.sidebar.slider("Price Ranger", price_min, price_max, price_max)

# Filtrando os livros que têm preço menor ou igual ao valor escolhido no slider
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
# Exibindo a tabela dos livros filtrados na interface principal
df_books

# Criando um gráfico de barras com a contagem de publicações por ano
fig = px.bar(df_books["year of publication"].value_counts())

# Criando um histograma com a distribuição dos preços dos livros
fig2 = px.histogram(df_books["book price"])

# Criando duas colunas lado a lado na interface
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
