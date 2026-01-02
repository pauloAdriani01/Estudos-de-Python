import os

#Biblioteca para melhorar a interface do terminal (Negrito nesse caso)
from rich import print

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

    nome_produto = input('Digite o nome do produto: ').capitalize()

    quantidade_produto = entrada_dados_numericos_inteiros(input('Digite a quantidade do produto: '))

    preço_produto = entrada_dados_numericos_floats(input('Digite o preço do produto: '))

    nome_dicionario = nome_produto.lower()

    estoque[nome_dicionario] = {
        'nome': nome_produto,
        'quantidade': quantidade_produto,
        'preço': preço_produto

    }

    os.system('cls')

    print(f'\nProduto {nome_produto} adicionado com sucesso!\n')
    print('Dados do produto adicionado:')

    print('-------------------------')

    for chave, valor in estoque[nome_dicionario].items():
        print(f'{chave.capitalize()}: {valor}')

    print('-------------------------')

    print()

    os.system('pause')

def ver_produto(estoque):
    os.system('cls')

    print('Opção selecionada: Ver um produto\n')

    nome_produto = input('Digite o nome do produto que deseja ver: ')

    nome_dicionario = nome_produto.lower()

    if encontrar_produto(estoque, nome_dicionario):
        os.system('cls')

        print(f'\nDados do produto {nome_produto.capitalize()}:')

        print('-------------------------')

        for chave, valor in estoque[nome_dicionario].items():
            print(f'{chave.capitalize()}: {valor}')
        
        print('-------------------------\n')

        os.system('pause')

    else:
        os.system('cls')

        print(f'\n[ERRO] Produto {nome_produto.capitalize()} não encontrado no estoque!')
        print('Voltando ao menu principal.\n')

        os.system('pause')

def ver_estoque(estoque):
    os.system('cls')

    print('Opção selecionada: Ver todo o estoque\n')

    print('Dados do estoque completo:\n')

    print('-------------------------')

    for chave, valor in estoque.items():
        print(f'[bold]Nome do Produto no Sistema:[/bold] {chave}')

        for chave_interna, valor_interno in valor.items():
            print(f'{chave_interna.capitalize()}: {valor_interno}')

        print('-------------------------')

    print()

    os.system('pause')

def atualizar_produto(estoque):
    os.system('cls')

    print('Opção selecionada: Atualizar um produto\n')

    nome_produto = input('Digite o nome do produto que deseja atualizar: ')

    nome_dicionario = nome_produto.lower()

    if encontrar_produto(estoque, nome_dicionario):
        os.system('cls')

        #Bold da biblioteca rich deixa o texto em negrito no terminal
        print(f'Atualizando dados do produto: [bold]{nome_dicionario}[/bold]\n')
        print('Dados atuais do produto:')

        for chave, valor in estoque[nome_dicionario].items():
            print(f'{chave.capitalize()}: {valor}')

        print('\nQue tipo de dado desejaria atualizar?')

        print('1 - Nome do Produto no Sistema (Nome do Dicionário)')
        print('2 - Nome do Produto (Valor do Dicionário)')
        print('3 - Quantidade do Produto')
        print('4 - Preço do Produto')
        print('5 - Voltar ao Menu Principal\n')

        opcao = entrada_dados_numericos_inteiros(input('Digite a opção desejada: '))

        match opcao:
            case 1:
                os.system('cls')

                novo_nome_produto_sistema = input('Digite o novo nome do produto no sistema: ').lower()

                estoque[novo_nome_produto_sistema] = estoque.pop(nome_dicionario)

                os.system('cls')

                print(f'Nome do produto no sistema atualizado com sucesso para: {novo_nome_produto_sistema}!')

                print('Voltando ao menu principal.\n')

                os.system('pause')

                return estoque

            case 2:
                os.system('cls')

                novo_nome_produto = input('Digite o novo nome do produto: ').capitalize()

                estoque[nome_dicionario]['nome'] = novo_nome_produto

                os.system('cls')

                print(f'Nome do produto atualizado com sucesso para: {novo_nome_produto}!')

                print('Voltando ao menu principal.\n')

                os.system('pause')

                return estoque

            case 3:
                os.system('cls')

                nova_quantidade_produto = entrada_dados_numericos_inteiros(input('Digite a nova quantidade do produto: '))

                if(nova_quantidade_produto is None):
                    return estoque

                estoque[nome_dicionario]['quantidade'] = nova_quantidade_produto

                os.system('cls')

                print(f'Quantidade do produto atualizada com sucesso para: {nova_quantidade_produto}!')

                print('Voltando ao menu principal.\n')

                os.system('pause')

                return estoque

            case 4:
                os.system('cls')

                novo_preco_produto = entrada_dados_numericos_floats(input('Digite o novo preço do produto: '))

                if(novo_preco_produto is None):
                    return estoque

                estoque[nome_dicionario]['preço'] = novo_preco_produto

                os.system('cls')

                print(f'Preço do produto atualizado com sucesso para: {novo_preco_produto}!')

                print('Voltando ao menu principal.\n')

                os.system('pause')

                return estoque

            case 5:
                os.system('cls')

                print('Voltando ao menu principal.\n')

                os.system('pause')

            case _:
                os.system('cls')

                print('[ERRO] Opção inválida!')
                print('Voltando ao menu principal.\n')

                os.system('pause')

def remover_produto(estoque):
    os.system('cls')

    print('Opção selecionada: Remover um produto\n')

    nome_produto = input('Digite o nome do produto que deseja remover: ').lower()

    if(encontrar_produto(estoque, nome_produto)):
        print(f'\nTem certeza que deseja remover o produto [bold]{nome_produto.lower()}[/bold] do estoque? (Y/N)')

        confirmacao = input('Digite sua opção: ').upper()

        match confirmacao:
            case 'Y':
                os.system('cls')

                estoque.pop(nome_produto)

                print(f'\nProduto [bold]{nome_produto.lower()}[/bold] removido com sucesso do estoque!')

                print('Voltando ao menu principal.\n')

                os.system('pause')

                return estoque

            case 'N':
                os.system('cls')

                print('Exclusão cancelada com sucesso.')

                print('Voltando ao menu principal.\n')

                os.system('pause')

            case _:
                os.system('cls')

                print('[ERRO] Opção inválida!')

                print('Voltando ao menu principal.\n')

                os.system('pause')

    else:
        os.system('cls')

        print(f'\n[ERRO] Produto {nome_produto.lower()} não encontrado no estoque!')
        print('Voltando ao menu principal.\n')

        os.system('pause')

def sair_sistema(estoque):
    os.system('cls')

    print('Obrigado por utilizar o sistema de estoque!\n')

    return False

#Funções de validação de entrada de dados

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

#Função para encontrar um produto no estoque
def encontrar_produto(estoque, nome_produto):
    for chave in estoque.keys():
        if chave == nome_produto:
            return True

    return False

#Posso apenas fazer isso:
'''
def encontrar_produto(estoque, nome_produto):
    if(nome_produto in estoque == True):
        return True

    else:
        return False

'''

#Não preciso retornar o dicionário principal nas funções, pois dicionários são mutáveis em Python

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

    if opcao is None:
        continue

    match opcao:
        case 1:
            adicionar_produto(estoque)

        case 2:
            ver_produto(estoque)

        case 3:
            ver_estoque(estoque)

        case 4:
            atualizar_produto(estoque)

        case 5:
            remover_produto(estoque)

        case 6:
            continuidade_menu = sair_sistema(estoque)

        case _:
            os.system('cls')

            print('[ERRO] Opção inválida!')
            print('Voltando ao menu principal.\n')

            os.system('pause')
