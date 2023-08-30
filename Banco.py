#Cod final do desafio Sistema bancario com explicações para estudos futuros
#Dev : Conceição Larissa 

class ContaBancaria:
    def __init__(self):
        self.saldo = 0  # Inicializa o saldo da conta como zero
        self.extrato = []  # Inicializa a lista de operações no extrato como vazia
        self.num_saques = 0  # Inicializa o contador de saques como zero

    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor  # Incrementa o saldo com o valor do depósito
            self.extrato.append(f"Depósito: +{valor}")  # Registra a operação no extrato
            print("Depósito realizado com sucesso.")
        else:
            print("Não é possível fazer depósito negativo.")

    def sacar(self, valor):
        if self.num_saques < 3 and valor <= 500 and self.saldo - valor >= 0:
            self.saldo -= valor  # Decrementa o saldo com o valor do saque
            self.extrato.append(f"Saque: -{valor}")  # Registra a operação no extrato
            self.num_saques += 1  # Incrementa o contador de saques
            print("Saque realizado com sucesso.")
        else:
            print("Não é possível fazer o saque.")

    def ver_extrato(self):
        for operacao in self.extrato:
            print(operacao)  # Exibe cada operação registrada no extrato
        print(f"Saldo atual: {self.saldo}")  # Exibe o saldo atual

    def sair(self):
        print("Saindo do sistema. Obrigado!")  # Exibe uma mensagem de saída

# Cria uma instância da classe ContaBancaria
conta = ContaBancaria()

while True:
    print("\nEscolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)  # Chama o método de depósito da instância da conta
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)  # Chama o método de saque da instância da conta
    elif opcao == "3":
        conta.ver_extrato()  # Chama o método de ver extrato da instância da conta
    elif opcao == "4":
        conta.sair()  # Chama o método de sair da instância da conta
        break  # Encerra o loop
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
