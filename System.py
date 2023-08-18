#Sistema Bancado de Operações: Sacar, Despositar e Visualizar Extratos
#Versão: v1
#Executará apenas com 1 usuário, sem questoes de agência e Conta

#Requisitos:
'''
Deposito: Todos os depósitos devem ser armazenados em uma variável e 
exibidos na operação extrato;

Saque: Permitir 3 saques diários com limite de R$500,00/saque | Caso não tenha saldo, 
exibirá uma msg| Todos os saques devem ser armazenados em uma variável e exibidos 
na operação extrato;

Extrato: Listar todos os depósitos e saques realizados na conta | No fim da listagem deve
ser exibido o saldo atual da conta(Exibidos em formato "R$xxx.xx").
'''

Menu = """
Olá, Bem vindo ao sistema bancário!

======== Menu =======
[d] depositar
[s] sacar
[e] extrato
[q] sair
=====================

"""


saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
contagem_saque = 3
extrato = ""

while True:

    opcao = input(Menu)
    
    if opcao == "d":
        valor = float(input('Informe o valor de depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print('Operação Falhou! O valor informado é invalido.')
        
    elif opcao == "s":
        
        print("\nSaldo: {:.2f}".format(saldo))
    
        print('\nO valor limite é de {} saques diários'.format(contagem_saque))
        print('\nO valor limite de cada saque é de R$ 500.00')

        valor = float(input('\nInforme o valor do saque: '))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou! Você não possui saldo o suficiente.')
        elif excedeu_limite:
            print('Operação falhou! o valor de saque excede o limite. ')
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques +=1
            contagem_saque -=1
        else:
            print('Operação Falhou! O valor informado é invalido.')

    elif opcao == "e":
        print('\n=================== EXTRATO ===================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}\n")
        print('=================================================')
    elif opcao == "q":
        break

    else:
        print('Número inválido, digite uma das opções selecionáveis!')
