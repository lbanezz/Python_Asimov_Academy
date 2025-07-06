import streamlit as st
import pandas as pd

df_reviews = pd.read_csv("datesets/customer reviews.csv")
df_top100_books = pd.read_csv("datesets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books, books")

df_book = df_top100_books[df_top100_books["book title"] == book]
df_book