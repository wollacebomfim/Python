# importar biblioteca para requisições http
import requests
import time
import random
# mostra o id do último grupo adicionado
def last_chat_id(token):
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(token)
        response = requests.get(url)
        if response.status_code == 200:
            json_msg = response.json()
            for json_result in reversed(json_msg['result']):
                message_keys = json_result['message'].keys()
                if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['message']['chat']['id']
            print('Nenhum grupo encontrado')
        else:
            print('A resposta falhou, código de status: {}'.format(response.status_code))
    except Exception as e:
        print("Erro no getUpdates:", e)

# enviar mensagens utilizando o bot para um chat específico
def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)
# token único utilizado para manipular o bot (não deve ser compartilhado)
# exemplo: '1413778757:AAFxmr611LssAHbZn1uqV_NKFsbwK3TT-wc'
token = '5369516714:AAGIkbhUXz055C2e0WzzHGHGt6LpXBEZNXw'

# id do chat que será enviado as mensagens
chat_id = -624956704
chat_id_2 = -750822818
chat_id_3 = -785747035


#id chat 1 = -624956704
#id chat 2 = -750822818
#id chat 3 = -785747035

print("Id do chat:", chat_id)
i = 1
while (i <= 9999999):
    time.sleep(60)
# exemplo de mensagem
    #msg = "Informações diarias: passando informações aos grupos, apenas vips podem ver"


    #msg = ['🏆Euro\n\n','⏰5.8.11.14\n\n','⚽️ Ambas marcam\n⚽️Over 2.5\n\n','🪙Opcionais moedinhas : \n\n2x2/3x0/3x1/3x2/4x0/ Viradinha / Outro resultados+5 /4 gols\n\n','💰Gestão: 0.50% 1% 2% 4%']
    #msg = ['🏆Euro\n','⏰5.8.11.14\n','⚽️ Ambas marcam\n','⚽️Over 2.5\n']
    #res = random.sample(msg, len(msg))
    #print(*res) 
    #msg = "🏆Euro\n\n\n⏰5.8.11.14\n\n\n⚽️ Ambas marcam\n\n\n⚽️Over 2.5\n\n\n🪙Opcionais moedinhas :\n\n\n2x2/3x0/3x1/3x2/4x0/ Viradinha / Outro resultados+5 /4 gols \n\n\n💰Gestão: 0.50% 1% 2% 4%"
    

    msg = "🏆Euro\n\n⏰5.8.11.14\n\n⚽️ Ambas marcam\n\n⚽️Over 2.5\n\n🪙Opcionais moedinhas :2x2/3x0/3x1/3x2/4x0/ Viradinha / Outro resultados +5 /4 gols\n\n💰Gestão: 0.50% 1% 2% 4%\n\n"
    
    
    
  

    send_message(token, chat_id, msg)
    send_message(token, chat_id_2, msg)
    send_message(token, chat_id_3, msg)
    i+= 1

    