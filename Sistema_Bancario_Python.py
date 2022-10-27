from ast import Break

menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
  opcao = input(menu).upper()

  if opcao == 'D'.upper():
    print('Depósito')
    valor = float(input('Digite o valor do depósito: '))
    if valor > 0:
      saldo += valor
      extrato += f'Depósito: R${valor:.2f}\n'
      print(f'Depósito de R${valor:.2f} realizado com sucesso.')
    else:
      print('Operação falhou! O valor informado é inválido.')
    
  elif opcao == 'S':
    print('Saque')
    valor = float(input('Digite o valor do saque: '))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES
    if excedeu_saldo:
      print('Operação Falhou! Você não possui saldo suficiente.')
    elif excedeu_limite:
      print('Operação Falhou! O valor do saque excedeu o limite.')
    elif excedeu_saques:
      print('Operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
      saldo -= valor
      extrato += f'Saque: R${valor:.2f}\n'
      numero_saques += 1
      print(f'Saque de R${valor:.2f} realizado com sucesso.')
    else:
      ('Operação inválida! Tente novamente.')

  elif opcao == 'E':
    print('\n==================== EXTRATO ==================== ')
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}\n')
    print('===================================================')
    

  elif opcao == 'Q':
    print('Saindo...')
    Break

  else:
    print('Operação inválida. Selecione novamente a operação desejada.')
