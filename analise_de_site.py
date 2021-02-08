# Programa de analise de dados de site
from bs4 import BeautifulSoup

import requests
#recebe o conteudo de requisição do site
site = requests.get("http:// ou https://nomedosite").content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())