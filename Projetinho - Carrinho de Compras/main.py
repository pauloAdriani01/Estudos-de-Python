'''
LISTAS SÃO UMA COLEÇÃO DE ITENS ORDENADOS E MUTÁVEIS, PODEM ARMAZENAR DUPLICATAS E DIFERENTES TIPOS
'''

import os

#Variáveis primeiro, depois as funções (ordem geral)

#Variável que controla o loop do menu
programaMenu = True

#Lista que armazenará os produtos do carrinho
meuCarrinho = []

def adicionarProduto(meuCarrinho):
    os.system('cls')

    tamanhoCarrinho = len(meuCarrinho)

    print("Opção Escolhida: Adicionar produto\n")

    print(f"Número de itens no carrinho: {tamanhoCarrinho}\n")

    print("Digite o nome do produto que deseja adicionar ao carrinho:")

    nomeProduto = input().strip()

    meuCarrinho.append(nomeProduto)
    
    print(f"\nO produto '{nomeProduto}' foi adicionado ao carrinho com sucesso!")
    print("Voltando ao menu.\n")

    os.system('pause')

def removerProduto(meuCarrinho):
    os.system('cls')

    tamanhoCarrinho = len(meuCarrinho)

    print("Opção Escolhida: Remover produto\n")

    if(tamanhoCarrinho == 0):
        print("Seu carrinho está vazio.")
        print("Voltando ao menu.\n")

        os.system('pause')

    else:
        print(f"Número de itens no carrinho: {tamanhoCarrinho}\n")

        print("Deseja mesmo remover um produto do carrinho? (S/N)")
        print("S --> Sim")
        print("N --> Não (Voltar ao menu)\n")

        escolhaRemoverProduto = input().upper()

        match escolhaRemoverProduto:
            case 'S':
                os.system('cls')

                print("Digite o nome do produto que deseja remover do carrinho:")
                nomeProduto = input().strip()

                if(nomeProduto in meuCarrinho):
                    meuCarrinho.remove(nomeProduto)

                    print(f"\nO produto '{nomeProduto}' foi removido do carrinho com sucesso!")
                    print("Voltando ao menu.\n")

                    os.system('pause')

                else:
                    print(f"\nO produto '{nomeProduto}' não foi encontrado no carrinho.")
                    print("Voltando ao menu.\n")

                    os.system('pause')

            case 'N':
                print("\nVoltando ao menu.\n")

                os.system('pause')

            case _:
                erroEntradaUsuario()

def visualizarCarrinho(meuCarrinho):
    os.system('cls')

    #Variável para guardar o tamanho da lista
    tamanhoCarrinho = len(meuCarrinho)

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

        escolhaVisualizarItens = input().upper()

        match escolhaVisualizarItens:
            case 'S':
                os.system('cls')

                print("Itens no carrinho:\n")

                meuCarrinho.sort()

                for item in meuCarrinho:
                    print(f"- {item}")

                print("\nVoltando ao menu.\n")

                os.system('pause')

            case 'N':
                print("\nVoltando ao menu.\n")

                os.system('pause')

            case _:
                erroEntradaUsuario()

def finalizarCompra(meuCarrinho):
    os.system('cls')

    tamanhoCarrinho = len(meuCarrinho)

    print("Opção Escolhida: Finalizar compra\n")

    print(f"Número de itens no carrinho: {tamanhoCarrinho}\n")

    print("Itens no carrinho:\n")

    meuCarrinho.sort()

    for item in meuCarrinho:
        print(f"- {item}")

    print("\nDeseja realmente finalizar a compra? (S/N)")
    print("S --> Sim")
    print("N --> Não (Voltar ao menu)\n")

    escolhaFinalizarCompra = input().upper()

    match escolhaFinalizarCompra:
        case 'S':
            meuCarrinho.clear()

            print("\nCompra finalizada com sucesso!")
            print("Obrigad@ por utilizar o Mercado Digital.\n")

            os.system('pause')

            return False

        case 'N':
            print("\nVoltando ao menu.\n")

            os.system('pause')

            return True

        case _:
            erroEntradaUsuario()

def sairPrograma(programaMenu):
    os.system('cls')

    print("Até mais! Obrigado por utilizar o Mercado Digital.\n")

    return False

def erroEntradaUsuario():
    os.system('cls')

    print("Opção inválida. Voltando ao menu.\n")

    os.system('pause')

    return True

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
                removerProduto(meuCarrinho)

            case 3:
                visualizarCarrinho(meuCarrinho)

            case 4:
                programaMenu = finalizarCompra(meuCarrinho)

            case 5:
                programaMenu = sairPrograma(programaMenu)

            case _:
                erroEntradaUsuario()
