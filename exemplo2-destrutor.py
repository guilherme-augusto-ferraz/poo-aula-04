
class Conta():
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def __del__(self):
        print(f"O objeto conta de número {self.numero} está sendo removido da memória")



conta1 = Conta("002000", "0026", 100)
print(conta1.saldo)
del(conta1)
