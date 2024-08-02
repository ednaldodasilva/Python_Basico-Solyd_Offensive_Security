from Classes import Cliente, Conta

#CRIANDO OS CLIENTES
clienteUm = Cliente("Ednaldo", "072.049.401-05", 21)
clienteDois = Cliente("Rosa", "819.934.631-00", 47)

#CRIANDO CONTA PARA OS CLIENTES
contaUm = Conta(clienteUm, 100.0, 5000.0)
contaDois = Conta(clienteDois,100.0, 5000.0)

#EXIBINDO INFORMAÇÕES DAS CONTAS
print(contaUm)
print(contaDois)

#REALIZANDO OPERAÇÕES NAS CONTAS
contaUm.depositar(550)
contaUm.sacar(250)
contaUm.consultarOsaldo()

contaDois.depositar(1000.0)
contaDois.sacar(3500.0) #Deve falhar devido a falta de dinheiro.
contaDois.consultarOsaldo()