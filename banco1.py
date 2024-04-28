class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.num_saques = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))
        else:
            print("Erro: Valor de depósito inválido.")

    def saque(self, valor):
        if self.num_saques < 3:
            if valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.num_saques += 1
                print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
            elif valor > self.saldo:
                print("Erro: Saldo insuficiente para realizar o saque.")
            else:
                print("Erro: Valor de saque excede o limite permitido (R$ 500).")
        else:
            print("Erro: Limite de saques diários excedido.")

    def extrato(self):
        print("\n--- Extrato ---")
        print("Depósitos:")
        for deposito in self.depositos:
            print("R$ {:.2f}".format(deposito))
        print("Saques:")
        for saque in self.saques:
            print("R$ {:.2f}".format(saque))
        print("\nSaldo atual: R$ {:.2f}".format(self.saldo))


# Função principal
def main():
    banco = Banco()

    while True:
        print("\nEscolha uma operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            banco.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            banco.saque(valor)
        elif opcao == '3':
            banco.extrato()
        elif opcao == '0':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
