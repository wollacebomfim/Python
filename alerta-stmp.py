import mysql.connector
import smtplib, ssl, getpass, datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import Message
from email.message import EmailMessage
from email.header import Header
import time
import os
import datetime

# myresult = mycursor.fetchall()

def check_value():

  print('Check_Value is called')

  mydb = mysql.connector.connect(
  host="", #host do servidor do banco de dados
  user="", #usuario do banco de dados
  password="", #senha do banco de dados
  database="") #base de dados do banco
  
  cursor = mydb.cursor()

  cursor.execute("SELECT * FROM sede WHERE id ORDER by id DESC LIMIT 1") #selecinando a database e procurando os valores
  print('Checando informações no banco...')
  time.sleep(5) 
  for row in cursor.fetchall():
    umi = row[1]
    temp = row[2]
    date = row[3]
  

    print('Valor apresentado da temperatura em check: {}'.format(str(temp)))
    
    #confirm_value(date, temp)
  time.sleep(2)  
  confirm_value(date, temp, umi)

def confirm_value(umi, temp, date):

  print('Confirm_Value is called')

  if temp >= 10:
    print('Confirmando as informações...')  
    time.sleep(5) 
    send_email(temp, date, umi)

  else:    
    print('A temperatura é inferior a 10.\nTemperatura atual é: {temp}')
    print('A Umidade atual é: {umi}')
    print('Aguardando 1 minutos para tentar novamente')
    time.sleep(60)


def get_html():

  message = MIMEMultipart("alternative")  
  html='''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<table style=" width: 100%; text-align: center;">
  <tr >   
      <td style="background-color: rgba(255, 255, 255, 1); width: 100%; text-align: center; padding: 100px 0px;">
          <table style=" width: 700px; margin: 0 auto; text-align: center; border-spacing: 0px;">
              
              <tr><td colspan="2" style=" width: 100%; text-align: center; padding: 10px; font-family: 'Work Sans', sans-serif; font-size: 25px;  color: #F9F9F9; background-color: #EA2614;                  ">Central de Automação e Operações</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: center;font-family: 'Work Sans', sans-serif; color: #fff; background-color: rgba(0, 173, 168, 1); font-size: 18px;"><img src="https://drive.google.com/uc?id=1xC0gv2-Mtvv1k8kAzZcH9674oo3EqOBp" width="31px" height="31px">&nbsp;Alerta de Temperatura e Umidade <style="width: 100%; text-align: right;font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(0, 173, 168, 1); font-size: 18px;"><img src="https://drive.google.com/uc?id=1xC0gv2-Mtvv1k8kAzZcH9674oo3EqOBp" width="31px" height="31px"></td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left; padding: 10px; font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1);            font-size: 14px;" ><br><br><b>Caros Analistas,</b> <br><br>Recebam as informações sobre o report...</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left; padding: 10px; font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;">Nossos logs indicam que um incidente em um de seus sensores.</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left; padding: 10px; font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;"><b>Informações do Evento:</b></td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left;font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;"><img src="https://drive.google.com/uc?id=1tfOoY1Q_tWfFhIZwKA4FNG08wzaXof07" width="25px" height="25px">&nbsp;&nbsp;&nbsp;&nbsp;<b>Umidade: </b>{temp}</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left;font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;"><img src="https://drive.google.com/uc?id=1xt4FEm6pm6WLjmEsySEOo4UCwEJHJBEu" width="31px" height="31px">&nbsp;&nbsp;<b>Temperatura: </b>{umi}</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left;font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;"><img src="https://drive.google.com/uc?id=1LkS5mZcdiyUOp3X4NZHcm2zsvu5PwvhY" width="25px" height="25px">&nbsp;&nbsp;&nbsp;&nbsp;<b>Data e hora do evento: </b>{date}</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: center; padding: 10px; font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;" >{Caso haja novos alertas você receberá outro e-mail notificando.}</td></tr>
              <tr><td colspan="2" style="width: 100%; text-align: left; padding: 10px; font-family: 'Work Sans', sans-serif; color: rgba(118,113,113,1); background-color: rgba(242, 242, 242, 1); font-size: 14px;" ><br><br>Atenciosamente,</td></tr>
              
          </table>
      </td>
  </tr>
</table>
'''

  return html, message

def send_email(umi, temp, date):

  html, message = get_html()
  umi = str(umi)
  temp = str(temp)
  date = str(date)

  html = html.replace('{umi}', umi)
  html = html.replace('{date}', date)
  html = html.replace('{temp}', temp)

  part2 = MIMEText(html, "html", _charset="UTF-8")
  message.attach(part2)

  

  print('Send_Value is called')
  print('Enviando email...')
  time.sleep(5)

  smtp_ssl_host = 'stmp do servidor de email: exemplo smtp.gmail.com'
  smtp_ssl_port = 465 #porta do servidor de email

  from_addr = 'automacao.qca@gmail.com'
  to_addrs = ['email que irá receber as informações do rpa'] 

  username = 'login que sera enviado'
  password = 'senha do email que vai ser enviado'

  message['subject'] = 'Alerta Temperatura CPD' 
  message['from'] = from_addr
  message['to'] = ', '.join(to_addrs)
  
  #informations = str('Alta temperatura detectada: %s\nData do ocorrido: %s' %(temp, date))

  try:    
    server = smtplib.SMTP_SSL(smtp_ssl_host,smtp_ssl_port)    
    server.login(username, password)    
    server.sendmail(from_addr, to_addrs, message.as_string())
    print('Email enviado')    
    server.close()
    time.sleep(60)
    check_value()
  except:
    print('ERROR no envio do email')
    check_value()
  
check_value()
