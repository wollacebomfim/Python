import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

request = urlopen(url)

info = json.load(request)

ip = info['ip']
org = info['org']
cidade = info['city']
pais = info['country']
regiao = info['region']

#imprimir as informações de ip externo do usuário
print('Detalhes do IP Externo \n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}'.format(org,regiao,pais,cidade,ip))