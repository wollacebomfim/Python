#Essa ferramenta indentifica a região do numero de telefone digitado dentro da variavel telefone.
import phonenumbers

from phonenumbers import geocoder

telefone = input('Digite o telefone no exemplo +55819000981:')

phone_number = phonenumbers.parse(telefone)

print('A localização do numero é de:',geocoder.description_for_number(phone_number, 'pt'))