'''
LISTAS SÃO UMA COLEÇÃO DE ITENS ORDENADOS E MUTÁVEIS, PODEM ARMAZENAR DUPLICATAS E DIFERENTES TIPOS
'''

import os

#Variáveis primeiro, depois as funções (ordem geral)

#Variável que controla o loop do menu
programaMenu = True

#Lista que armazenará os produtos do carrinho
meuCarrinho = []

#Variável para guardar o tamanho da lista
tamanhoCarrinho = len(meuCarrinho)

def adicionarProduto(meuCarrinho):
    os.system('cls')

    print("Opção Escolhida: Adicionar produto\n")

    print(f"Número de itens no carrinho: {tamanhoCarrinho}\n")

    print("Digite o nome do produto que deseja adicionar ao carrinho:")

    nomeProduto = input().strip()

    meuCarrinho.append(nomeProduto)
    
    print(f"\nO produto '{nomeProduto}' foi adicionado ao carrinho com sucesso!")
    print("Voltando ao menu.\n")

    os.system('pause')


def visualizarCarrinho(meuCarrinho):
    os.system('cls')

    print("Opção Escolhida: Visualizar carrinho\n")

    if(tamanhoCarrinho == 0):
        print("Seu carrinho está vazio.")
        print("Voltando ao menu.\n")

        os.system('pause')   

    else:
        print(f"Número de itens no carrinho: {tamanhoCarrinho}\n")

        print("Gostaria de visualizar os itens do carrinho? (S/N)")
        print("S --> Sim")
        print("N --> Não (Voltar ao menu)\n")

        try:
            escolhaVisualizarItens = input().upper()
            
        except ValueError:
            erroEntradaUsuario()

        else:
            match escolhaVisualizarItens:
                case 'S':
                    pass

                case 'N':
                    print("\nVoltando ao menu.\n")

                    os.system('pause')

                case _:
                    erroEntradaUsuario()

def sairPrograma(programaMenu):
    os.system('cls')

    print("Até mais! Obrigado por utilizar o Mercado Digital.\n")

    return False

def erroEntradaUsuario():
    _= os.system('cls')

    print("Opção inválida. Voltando ao menu.\n")

    _= os.system('pause')

while programaMenu == True:
    os.system('cls')

    print("Seja bem-vind@ ao seu carrinho do Mercado Digital!")
    print("Aqui você pode adicionar ou remover produtos,  visualizar seu carrinho e finalizar a sua compra.\n")

    print("O que deseja fazer?\n")

    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Visualizar carrinho")
    print("4 - Finalizar compra")
    print("5 - Sair\n")

    try:
        #Variável que guarda a entrada da escolha do usuário
        escolhaUsuarioMenu = int(input())

    except ValueError:
        erroEntradaUsuario()

    else:
        match escolhaUsuarioMenu:
            case 1:
                adicionarProduto(meuCarrinho)
            
            case 2:
                pass

            case 3:
                visualizarCarrinho(meuCarrinho)

            case 4:
                pass

            case 5:
                programaMenu = sairPrograma(programaMenu)

            case _:
                erroEntradaUsuario()
