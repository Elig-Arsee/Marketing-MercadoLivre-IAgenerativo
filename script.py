# -*- coding: utf-8 -*-
"""script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/134dT5Yf46AmUzs-A_G-8J7a_LkU5u4FF

# ETL com Python
Projeto de Extração, transformação e carregamento de dados.

1. Extrair dados com raspagem de dados dos itens do Mercado Livre
"""

# Instalando bibliotecas
import requests
from bs4 import BeautifulSoup

# URL do Mercado Livre com produtos em promoção
url = 'https://www.mercadolivre.com.br/ofertas'

# Realizando uma solicitação GET à página
response = requests.get(url)

# Analisando o conteúdo da página usando BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extrai informações relevantes dos produtos (título, preço original, desconto e preço final)
produtos = []
for produto in soup.find_all('a', class_='promotion-item__link-container'):
    titulo_elem = produto.find('p', class_='promotion-item__title')
    titulo = titulo_elem.text.strip() if titulo_elem else ''

    preco_original_elem = produto.find('s', class_='andes-money-amount')
    preco_original_text = preco_original_elem.text.strip() if preco_original_elem else '0'
    preco_original_words = preco_original_text.split()
    preco_original_value = preco_original_words[-1]  # Pega a última palavra após a divisão
    preco_original = float(preco_original_value.replace('R$', '').replace('.', '').replace(',', '.').replace('reales', ''))

    desconto_elem = produto.find('span', class_='andes-money-amount__discount')
    desconto = int(desconto_elem.text.strip().replace('% OFF', '')) if desconto_elem else 0

    preco_final_elem = produto.find('span', class_='andes-money-amount__fraction')
    preco_final = float(preco_final_elem.text.strip().replace('R$', '').replace('.', '').replace(',', '.')) if preco_final_elem else 0.0

    link_produto = produto['href'] # Extrai o link da página do produto



    produtos.append({'titulo': titulo, 'preco_original': preco_original, 'desconto': desconto, 'preco_final': preco_final, 'link_produto':link_produto})

# Importando pandas
import pandas as pd

# Transformando em df
df = pd.DataFrame(produtos)

# Visualizando os dados coletados e transformados em df
print(df.head())

"""2. Transformação dos dados"""

# Selecionando colunas relevantes
df = df[['titulo', 'preco_original', 'desconto', 'preco_final', 'link_produto']]

# Calculando o desconto em reais
df['desconto_absoluto'] = df['preco_original'] - df['preco_final']

# Visualizando os dados transformados
print(df.head())

"""3. Geração de Mensagens Personalizadas com IA Generativa"""

# instalando e importando openai
!pip install openai

# Importando openai
import openai

# Configure sua chave de API da OpenAI
api_key = 'sua chave api'

# Função para gerar mensagens personalizadas
def gerar_mensagem_personalizada(titulo, desconto, preco_final, link_produto):
    return f"Aproveite agora!{titulo} com {desconto}% de desconto. Compre agora por R${preco_final} clicando aqui {link_produto}."

# Aplicando a geração de mensagens personalizadas
df['mensagem_marketing'] = df.apply(lambda row: gerar_mensagem_personalizada(row['titulo'], row['desconto'], row['preco_final'], row['link_produto']), axis=1)

# Configurando o pandas para exibir o texto completo da coluna 'mensagem_marketing'
pd.set_option('display.max_colwidth', None)

# Visualizando as mensagens personalizadas
print(df['mensagem_marketing'].head())

"""3. Convertendo df em csv (incluindo as mensagens enviadas)"""

# Especificando o nome do arquivo CSV
nome_arquivo_csv = 'projeto_ETL_IA_generativa.csv'

# Salvando os dados do df em um arquivo CSV
df.to_csv(nome_arquivo_csv, index=False)

print(f'Dados salvos em "{nome_arquivo_csv}"')

# Baixando csv
from google.colab import files
files.download(nome_arquivo_csv)

# Gerando arquivo de requisitos
!pip freeze > requirements.txt

from google.colab import files
files.download('requirements.txt')
