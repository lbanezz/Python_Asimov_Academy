# Python_Asimov_Academy
Curso básico de python

# 📚 Book Dashboard

Este projeto consiste em um **dashboard interativo de livros** desenvolvido com **Python + Streamlit**, que permite explorar dados de livros populares e suas avaliações, com visualizações dinâmicas, filtros e métricas.

## 🎯 Objetivo

Fornecer uma ferramenta visual e intuitiva para:

* Filtrar livros por gênero, preço e ano de publicação
* Analisar distribuições e tendências
* Visualizar métricas como avaliação média
* Observar os livros mais bem avaliados

---

## 🛠️ Tecnologias Utilizadas

* Python 3.8+
* [Streamlit](https://streamlit.io/)
* Pandas
* Plotly

---

## 📁 Estrutura do Projeto

```
BookDashboard/
├── app.py                     # Arquivo principal com navegação entre páginas
├── pages/
│   ├── Livros.py              # Página com filtros, métricas e gráficos
│   └── Analises.py            # Página com estatísticas e rankings
├── utils/
│   └── loader.py             # Função de carregamento de dados (com cache)
├── datesets/                 # Dados brutos em CSV
│   ├── Top-100 Trending Books.csv
│   └── customer reviews.csv
├── assets/
│   └── logo.png              # Logotipo da aplicação
├── requirements.txt          # Dependências do projeto
```

---

## 🚀 Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/book-dashboard.git
cd book-dashboard
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

---

## 📊 Funcionalidades

### Página "Livros"

* Filtro por **preço**, **gênero** e **ano de publicação**
* Tabela com os livros filtrados
* Gráfico de publicações por ano
* Histograma de preços
* Média de avaliação dos livros selecionados

### Página "Análises"

* Média de avaliação por gênero
* Top 10 livros mais bem avaliados
* Distribuição das notas dos clientes

---

## 📥 Fontes dos Dados

* `Top-100 Trending Books.csv`: lista de livros populares com informações de título, autor, gênero, preço, nota e ano
* `customer reviews.csv`: base com avaliações de clientes

---

## 🧠 Autor

Desenvolvido por **\[Seu Nome]**, apaixonado por dados, tecnologia e projetos visuais.

[![LinkedIn](https://www.linkedin.com/in/david-reis-029027123/)

---

## 📌 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
