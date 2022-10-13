from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-'*14)
print('J O K E N P O')
print('-'*14)
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
esc = int(input('Qual sua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*14)
print('JOGADOR escolheu {}'.format(itens[esc]))
print('COMPUTADOR escolheu {}'.format(itens[computador]))
print('-='*14)
if esc == 0 and computador == 2 or esc == 2 and computador == 1 or esc == 1 and computador == 0:
    print('JOGADOR VENCEU')
elif computador == 0 and esc == 2 or computador == 2 and esc == 1 or computador == 1 and esc == 0:
    print('COMPUTADOR VENCEU')
elif esc == computador:
    print('EMPATE')
else:
    print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE.')



