
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

    def consultar_saldo(self):
        return super().consultar_saldo() + self.rendimento

    def gerar_rendimento(self, taxa):
        self.rendimento = self.rendimento + super().consultar_saldo() * taxa / 100
        return self.rendimento


class LimiteConta:
    def colocarLimite(self, conta, valor):
        conta.limite = conta.consultar_saldo() + valor


conta1 = ContaPoupanca("002000", "0026", 100)
print(conta1.gerar_rendimento(15))

conta2 = ContaPoupanca("009999", "0026", 300)
print(conta2.gerar_rendimento(12))

limite = LimiteConta()
limite.colocarLimite(conta1, 1000)

print(conta1.limite)
# print(conta2.limite)
# limite.colocarLimite(conta2, 2000)
# print(conta2.limite)

