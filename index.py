menu = """
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
"""

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    #depósito
    if opcao == "d":
        valor = float(input('Informe o valor do depósito:'))
        
        if valor > 0:
            saldo += valor
            extrato = print(f'Depósito R$ {valor:.2f}')
        else:
            print('Erro: Valor de depósito inválido.')
    #saque
    elif opcao == "s":
        valor = float(input('Informe o valor do saque:'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Falha! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Falha! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Falha! Você já atingiu o limite de saques hoje.')
        elif valor > 0:
            saldo -= valor
            extrato = f'Saque R$ {valor:.2f}'
            numero_saques += 1
        else:
            print('Erro: Valor de saque inválido. Tente novamente.')
    #extrato
    elif opcao == "e":
        print("\n ============== Extrato ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo R$ {saldo:.2f}')
        print('===================================')
    #sair
    elif opcao == "q":
        print('Obrigado! Volte sempre!')
        break
    #Erro
    else:
        print('Erro: Opção inválida. Por favor, selecione novamente a operação desejada.')
