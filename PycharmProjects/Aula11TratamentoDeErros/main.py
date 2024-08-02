import time

#def reverse():

#def reverso():

def abrirArquivo():
    try:
        arquivo = open('arquivo.txt')
        return True
    except Exception as Erro:
        print("Aconteceu algo de errado!", Erro)
        return False

while not abrirArquivo():
    print("Tentando abrir arquivo!")
    time.sleep(5)
print('Arquivo aberto com sucesso!')


#try:
    #d = 2/0
#except ZeroDivisionError:
    #print("Divisão por zero! Não tem como resolver...")

#try:
    #reverse()
#except Exception as Error:
    #print("Nome da função está errada!")

#try:
    #reverso()
#except NameError as Error:
    #print("Nome da função está errada!")
