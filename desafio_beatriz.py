# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 1  # Contador para contas

# Funções
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def extrato_bancario():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Operação falhou! CPF já cadastrado.")
        return

    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso!")

def criar_conta(cpf):
    global numero_conta
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario:
        contas.append({
            'agencia': "0001",
            'numero_conta': numero_conta,
            'usuario': usuario
        })
        print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
        numero_conta += 1
    else:
        print("Operação falhou! Usuário não encontrado.")

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
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        extrato_bancario()

    elif opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (apenas números): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
