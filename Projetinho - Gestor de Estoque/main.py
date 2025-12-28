import os

'''
DICIONÁRIO SÃO ORDENADOS, MUTÁVEIS E NÃO PERMITEM VALORES DUPLICADOS
'''

continuidade_menu = True

#Criando o "dicionário principal" com alguns produtos já inseridos nele
estoque = {
    'teclado': {
        'nome': 'Teclado',
        'quantidade': 10,
        'preço': 250.00

    },

    'mouse': {
        'nome': 'Mouse',
        'quantidade': 15,
        'preço': 150.00

    },

    'monitor': {
        'nome': 'Monitor',
        'quantidade': 5,
        'preço': 1250.00

    }

}

#Menu principal do sistema
while continuidade_menu == True:
    os.system('cls')

    print('=== SISTEMA DE ESTOQUE ===')
    print('Olá! Como gostaria de prosseguir?\n')

    print('1 - Adicionar produto')
    print('2 - Ver um produto')
    print('3 - Ver todo o estoque')
    print('4 - Atualizar um produto')
    print('5 - Remover um produto')
    print('6 - Sair do sistema\n')

    try:
        opcao = int(input('Digite a opção desejada: '))

    except ValueError:
        os.system('cls')

        print('[ERRO] Opção inválida!')
        print('Voltando ao menu principal.\n')

        os.system('pause')

        continue

    else:
        match opcao:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

            case 6:
                pass

            case _=
                pass
