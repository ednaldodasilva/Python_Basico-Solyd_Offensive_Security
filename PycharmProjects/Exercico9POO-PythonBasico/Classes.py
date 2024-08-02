class Cliente:
    def __init__(self, nome: str, cpf: int, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Idaede: {self.idade}"

class Conta:
    def __init__(self, cliente: Cliente, saldo: float, limite: float):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor: float):
        if valor < 0:
            print("O valor do saque deve ser acima de R$ OO,OO !")
            return False

        if valor > self.saldo + self.limite:
            print("Não foi possivel concluir essa operação!")
            return False

        self.saldo += valor
        print(f"Saque de {valor} finalizado com sucesso. Saldo disponivel: {self.saldo}")
        return True

    def depositar(self, valor: float):
        if valor <= 0:
            print("O valor deve ser positivo para prosseguir!")
            return False
        self.saldo += valor
        print(f"Deposito de valor {valor} realizado com exito. Saldo atual: {self.saldo}")
        return True

    def consultarOsaldo(self):
            print(f"O saldo atual é: {self.saldo}")
            return self.saldo

    def __str__(self):
            return f"Conta de {self.cliente.nome} - Saldo: {self.saldo}. LImite: {self.limite}"

