
class Conta():
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo


class ContaPoupanca(Conta):
    def __init__(self, numero, agencia, saldo):
        super().__init__(numero, agencia, saldo)
        self.rendimento = 10

    def consultar_rendimento(self):
        return self.rendimento



conta1 = ContaPoupanca("002000", "0026", 100)
print(conta1.saldo)
print(conta1.consultar_saldo())
print(conta1.consultar_rendimento())