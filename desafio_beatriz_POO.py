from datetime import date

# Classe Transacao (interface)
class Transacao:
    def registrar(self, conta):
        pass

# Classes Cliente e PessoaFisica (herança)
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe Conta
class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.cliente = cliente
        self.numero = numero
        self.agencia = agencia
        self.historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        return False

# Classe ContaCorrente (herança)
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = 3
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > 0:
            if self.saldo + self.limite >= valor and self.numero_saques < self.limite_saques:
                self.saldo -= valor
                self.historico.adicionar_transacao(Saque(valor))
                self.numero_saques += 1
                return True
        return False

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Classes Deposito e Saque (implementam Transacao)
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

# Funções para interação com o sistema (menu e operações)
def realizar_transacao(conta, transacao):
    transacao.registrar(conta)

def adicionar_conta(cliente, numero):
    contas.append(Conta(cliente, numero, "0001"))

# Variáveis globais
usuarios = []
contas = []
numero_conta = 1

# Menu
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar Usuário
[c] Criar Conta
[q] Sair
=> """

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta_selecionada = int(input("Informe o número da conta: ")) - 1
        if contas[conta_selecionada].depositar(valor):
            realizar_transacao(contas[conta_selecionada], Deposito(valor))
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        conta_selecionada = int(input("Informe o número da conta: ")) - 1
        if contas[conta_selecionada].sacar(valor):
            realizar_transacao(contas[conta_selecionada], Saque(valor))
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! Saldo insuficiente ou limite de saques atingido.")

    elif opcao == "e":
        for conta in contas:
            print(f"Conta {conta.numero}: Saldo R$ {conta.saldo:.2f}")

    elif opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (apenas números): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios.append(PessoaFisica(nome, data_nascimento, cpf, endereco))
        print("Usuário cadastrado com sucesso!")

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        usuario_encontrado = next((usuario for usuario in usuarios if usuario.cpf == cpf), None)
        if usuario_encontrado:
            adicionar_conta(usuario_encontrado, numero_conta)
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
            numero_conta += 1
        else:
            print("Operação falhou! Usuário não encontrado.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
