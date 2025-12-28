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

def adicionar_produto(estoque):
    os.system('cls')

    print('Opção selecionada: Adicionar um produto\n')

    nome_produto = input('Digite o nome do produto: ')

    quantidade_produto = entrada_dados_numericos_inteiros(input('Digite a quantidade do produto: '))

    preço_produto = entrada_dados_numericos_floats(input('Digite o preço do produto: '))

    nome_dicionario = nome_produto.lower()

    estoque[nome_dicionario] = {
        'nome': nome_produto,
        'quantidade': quantidade_produto,
        'preço': preço_produto

    }

    print(f'\nProduto {nome_produto} adicionado com sucesso!\n')
    print('Dados do produto adicionado:')

    print('-------------------------')

    for chave, valor in estoque[nome_dicionario].items():
        print(f'{chave.capitalize()}: {valor}')

    print('-------------------------')

    os.system('pause')

#Funções para evitar erros na entrada de dados do usuário
def entrada_dados_numericos_inteiros(dado):
    try:
        dado = int(dado)

    except ValueError:
        os.system('cls')

        print('[ERRO] Opção inválida!')
        print('Voltando ao menu principal.\n')

        os.system('pause')

        return None

    else:
        return dado

def entrada_dados_numericos_floats(dado):
    try:
        dado = float(dado)

    except ValueError:
        os.system('cls')

        print('[ERRO] Opção inválida!')
        print('Voltando ao menu principal.\n')

        os.system('pause')

        return None

    else:
        return dado

#Menu principal do sistema
while continuidade_menu == True:
    os.system('cls')

    print('=== SISTEMA DE ESTOQUE ===')
    print('Olá! Como gostaria de prosseguir?\n')

    print('1 - Adicionar um produto')
    print('2 - Ver um produto')
    print('3 - Ver todo o estoque')
    print('4 - Atualizar um produto')
    print('5 - Remover um produto')
    print('6 - Sair do sistema\n')

    opcao = entrada_dados_numericos_inteiros(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            adicionar_produto(estoque)

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

        case _:
            pass
