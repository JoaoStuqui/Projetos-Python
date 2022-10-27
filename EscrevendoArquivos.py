while True:
    escolha = int(input('''
    [1] Escrever no arquivo
    [2] Ler o arquivo
    '''))
    if escolha == 1:
        arquivo = open('arquivo', 'a')
        arquivo.write(input('Digite o que inserir no arquivo: ')) 
    elif escolha == 2:
        arquivo = open('arquivo', 'r')
        print(arquivo.readlines())
    else:
        print('Opção inválida. Escolha novamente')
    saida = input('Quer continuar? [S/N]').upper()
    if saida == 'N':
        break
    elif saida == 'S':
        print('Continuando...')
    else:
        print('Opção Inválida.')
