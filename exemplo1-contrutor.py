
class Conta():
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo



conta1 = Conta("002000", "0026", 100)
print(conta1.saldo)