import os
from shutil import copyfile
while True:
    escolha = int(input('''
    [1] Escrever no arquivo
    [2] Ler o arquivo
    [3] Deletar o arquivo
    '''))
    if escolha == 1:
        arquivo = open('arquivo', 'a')
        arquivo.write(input('Digite o que inserir no arquivo: ')) 
        arquivo.close()
    elif escolha == 2:
        arquivo = open('arquivo', 'r')
        print(arquivo.readlines())
        arquivo.close()
    elif escolha == 3:
        copyfile('arquivo', 'arquivo2')
        os.remove("arquivo")
    else:
        print('Opção inválida. Escolha novamente')
    
    saida = input('Quer continuar? [S/N]').upper()
    if saida == 'N':
        break
    elif saida == 'S':
        print('Continuando...')
    else:
        print('Opção Inválida.')
