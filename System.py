#Sistema Bancado de Operações: Sacar, Despositar e Visualizar Extratos
#Versão: v2
#Executará com funções gerenciando operações bancárias e criando e gerenciando usuários, com uma agência fixa

#Requisitos:
'''
Deposito: Todos os depósitos devem ser armazenados em uma variável e
exibidos na operação extrato;

Saque: Permitir 3 saques diários com limite de R$500,00/saque | Caso não tenha saldo,
exibirá uma msg| Todos os saques devem ser armazenados em uma variável e exibidos
na operação extrato;

Extrato: Listar todos os depósitos e saques realizados na conta | No fim da listagem deve
ser exibido o saldo atual da conta(Exibidos em formato "R$xxx.xx").

Usuário: Criara um novo usuário o listará.

Conta: Criara mais de uma conta para um mesmo titular, diferenciando titulares por seus CPFs
'''

import textwrap
from time import sleep

def menu():
    menu = """
    ======= MENU =====   
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    → """
    return input(textwrap.dedent(menu)).lower()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR${valor:.2f}\n'
        print('\n== Depósito realizado com sucesso! ==')
        sleep(2)
    else:
        print('\n@@@ Operação falhou! O calor informado é inválido. @@@')
        sleep(2)

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')
        sleep(2)

    elif excedeu_limite:
        print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@')
        sleep(2)

    elif excedeu_saques:
        print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')
        sleep(2)

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
        sleep(2)

    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
        sleep(2)

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n======= EXTRATO =======')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=' * 23)
    sleep(2)


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente em números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe usuário com esse CPF! @@@')
        sleep(2)
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco': endereco})

    print('== Usuário criado com sucesso! ==')
    sleep(2)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    sleep(0.5)
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n== Conta criada com sucesso! ==')
        sleep(2)
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@')
    sleep(2)

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Títular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))
        sleep(2)
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe um valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')
            sleep(2)

main()