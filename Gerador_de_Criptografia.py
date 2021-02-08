import hashlib

recebe = input ("Digite a senha que será critografada: ")

menu = int(input
(''' # Escolha a criptografia #
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o numero para a senha ser criptograda: '''))


if menu == 1:
    resultado = hashlib.md5(recebe.encode('utf-8'))
    print('A senha', recebe, 'foi criptografada em (MD5) e agora é:',resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(recebe.encode('utf-8'))
    print('A senha', recebe, 'foi criptografa em (SHA1) e agora é:',resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(recebe.encode('utf-8'))
    print('A senha', recebe, 'foi criptografa em (SHA256) e agora é:',resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(recebe.encode('utf-8'))
    print('A senha', recebe, 'foi criptografa em (SHA512) e agora é:',resultado.hexdigest())

else: 
    print('Algo deu errado, tente novamete !')