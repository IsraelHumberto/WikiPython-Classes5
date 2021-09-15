# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero
# e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo=0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo
        self.opcao_conta()

    def alterarNome(self):
        self.nome = input('Digite seu nome: ')
        print(f'O nome da sua conta foi alterado para: {self.nome.title()}\n')

    def informacoes(self):
        print('-' * 30 + '\n')
        print('TIPO DE CONTA: Corrente\n'
              f'NUMERO DA CONTA: {self.numero_conta}\n'
              f'NOME: {self.nome}\n'
              f'SALDO: {self.saldo}')
        print('-' * 30 + '\n')

    def deposito(self, valor_depositado=0):
        self.valor_depositado = float(input('Digite o valor do depósito: '))
        self.saldo += self.valor_depositado
        print(f'O seu novo saldo é: {self.saldo}')

    def saque(self, valor_saque=0):
        self.valor_saque = float(input('Digite o valor do saque: '))
        if self.valor_saque > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= self.valor_saque
            print(f'Seu novo saldo é: {self.saldo}\n')

    def opcao_conta(self, opcao=0):
        print(f'Olá, {self.nome.title()}, seja bem vindo(a)\n'
              f'----------------------------------------------')
        self.opcao = int(input('Digite a opção desejada:\n'
                               '1 - Alteração de nome\n'
                               '2 - Mostrar informações\n'
                               '3 - Saque\n'
                               '4 - Depósito\n'))

        if self.opcao == 1:
            self.alterarNome()
        elif self.opcao == 2:
            self.informacoes()
        elif self.opcao == 3:
            self.saque()
        elif self.opcao == 4:
            self.deposito()



