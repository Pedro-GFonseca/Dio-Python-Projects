menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 1800
limite = 500
extrato = f''
numero_saques = 0
LIMITE_SAQUES = 3
notas = [5, 10, 20, 50, 100]

while True:
    
    opcao = input(menu)
    
    match opcao:
        case 'd':
            try:
                valor = float(input('Informe o valor a ser depositado: '))
                
                if valor > 0:
                    saldo += valor
                    extrato += f'Depósito: R$ {valor:.2f}\n'
                    print('Depósito realizado com sucesso.')
                else:
                    print('Operação falhou! O valor informado é inválido.')
            except ValueError:
                print('Entrada inválida.')
            
        case 's':
            try:
                valor = float(input('Informe o valor a ser sacado: '))
                if valor % min(notas) == 0:
                
                    if valor > 0 and valor <= 500:
                        if saldo >= valor and numero_saques < LIMITE_SAQUES:
                            saldo -= valor
                            extrato += f'Saque: R$ {valor:.2f}\n'
                            numero_saques += 1
                            print('Saque realizado com sucesso.')
                        else:
                            print('Operação falhou! Saldo insuficiente ou limite de saques diários atingido.')
                    else:
                        print('Operação falhou! O valor inserido para saque é inválido.')
                else:
                    print(f'O valor informado é inválido. Notas disponíveis para saque: {notas}')
            except ValueError:
                print('Entrada inválida.')
        case 'e':
            print('=============== EXTRATO ===============')
            print('Não foram realizadas movimentações.' if not extrato else extrato)
            print('=======================================')
            print(f'Saldo: {saldo}')
        case 'q':
            print('Encerrando a sessão.')
            break
        case default:
            print('Opção inválida.')