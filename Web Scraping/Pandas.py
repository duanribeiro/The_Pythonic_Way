import pandas as pd
import requests
from bs4 import BeautifulSoup

# Primeiro, vamos pegar as informações do nosso site. / First, we have to download the info in our website.
informacoes_geral = pd.read_csv('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_201812.csv', encoding='utf8', sep=';')

# Depois temos que filtrar nossas informações, nesse exemplo vou buscar pelo cnpj do fundo. / After, we had to filter our info by some unique identifier
informacoes_fundo = informacoes_geral[informacoes_geral['CNPJ_FUNDO'] == '00.017.024/0001-53']

# Salvar as informações em um arquivo. / Save the info into a file
informacoes_fundo.to_csv('Informacões do Fundo', encoding='latin-1', index=False)

# Carregar o site de noticias na internet
noticias_web = requests.get('https://economia.uol.com.br/noticias/')

# Traduzir o site, em um formato legível
noticias_web_convertido = BeautifulSoup(noticias_web.text, 'html.parser')

# Utilizar o identificador para achar nossa informação
todos_titulo_noticia = noticias_web_convertido.find_all(class_='thumb-title')

# Ele irá retornar todos os títulos que existem na página, porém vamos selecionar apenas o primeiro.
primeiro_titulo_noticia = todos_titulo_noticia[0].text