'''
TUPLAS SÃO ORDENADAS E IMUTÁVEIS (NÃO PODEM SER MODIFICADAS APÓS SUA CRIAÇÃO)
'''

import os

continuidade_menu = True

lista_alunos = []

def adicionar_aluno(lista_alunos):
    os.system('cls')

    print("Opção Escolhida: Adicionar aluno")
    print("Atenção: dados incorretos não poderão ser alterados posteriormente!\n")

    ID_aluno = input("Digite o ID do aluno: ")

    nome_aluno = input("\nDigite o nome do aluno: ")

    nota1_aluno = float(input("\nDigite a primeira nota do aluno: "))

    nota2_aluno = float(input("\nDigite a segunda nota do aluno: "))

    aluno = (ID_aluno, nome_aluno, nota1_aluno, nota2_aluno)

    lista_alunos.append(aluno)

    print(f"\nAluno {nome_aluno} de ID {ID_aluno} adicionado com sucesso!")

    print("Voltando ao menu principal.\n")

    os.system('pause')

    return lista_alunos

#Função para não permitir inserir IDs iguais na lista de alunos
def verificar_ID_aluno():
    pass

def visualizar_aluno(lista_alunos):
    os.system('cls')

    print("Opção Escolhida: Visualizar um aluno específico\n")

    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado no sistema.\n")

        print("Voltando ao menu principal.")
        os.system('pause')

        return
    
    else:
        try:
            ID_aluno_busca = input("Digite o ID do aluno que deseja visualizar: ")

        except ValueError:
            os.system('cls')

            print("[ERRO]Valor inválido!")
            print("Voltando ao menu principal.\n")

            os.system('pause')

        else:

            if ID_aluno_busca not in [aluno[0] for aluno in lista_alunos]:
                os.system('cls')

                print(f"[ERRO]Aluno de ID {ID_aluno_busca} não encontrado no sistema.\n")

                print("Voltando ao menu principal.")
                os.system('pause')

            else:
                for aluno in lista_alunos:
                    indice_aluno_lista = 0

                    if aluno[0] == ID_aluno_busca:
                        os.system('cls')

                        print("Dados do Aluno Buscado:\n")

                        print(f"ID: {aluno[0]}")
                        print(f"Nome: {aluno[1]}")
                        print(f"Nota 1: {aluno[2]}")
                        print(f"Nota 2: {aluno[3]}\n")

                        print("Voltando ao menu principal.")
                        os.system('pause')

def visualizar_todos_alunos(lista_alunos):
    os.system('cls')

    print("Opção Escolhida: Visualizar todos os alunos\n")

    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado no sistema.\n")

        print("Voltando ao menu principal.")
        os.system('pause')

        return

    else:
        print("Lista de Todos os Alunos Cadastrados:\n")

        for aluno in lista_alunos:
            print("---------------")
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Nota 1: {aluno[2]:.2f}")
            print(f"Nota 2: {aluno[3]:.2f}")

        print("---------------\n")

        print("Voltando ao menu principal.")
        os.system('pause')

def calcular_media_aluno(lista_alunos):
    pass

while continuidade_menu == True:
    os.system('cls')

    print("--- Sistema de Gerenciamento de Registros de Alunos ---\n")

    print("Seja bem-vind@ ao nosso sistema de gerenciamento de registros de alunos!")
    print("O que gostaria de fazer?\n")

    print("1 - Adicionar aluno")
    print("2 - Visualizar um aluno específico")
    print("3 - Visualizar todos os alunos")
    print("4 - Calcular a média de um aluno")
    print("5 - Remover um aluno")
    print("6 - Sair do sistema\n")

    try:
        opcao_menu = int(input(""))

    except ValueError:
        os.system('cls')

        print("[ERRO]Valor inválido!")
        print("Voltando ao menu.\n")

        os.system('pause')

        continue

    else:
        match opcao_menu:
            case 1:
                lista_alunos = adicionar_aluno(lista_alunos)

            case 2:
                visualizar_aluno(lista_alunos)

            case 3:
                visualizar_todos_alunos(lista_alunos)

            case 4:
                calcular_media_aluno(lista_alunos)

            case 5:
                pass

            case 6:
                os.system('cls')

                print("Obrigado por utilizar nosso sistema!")
                print("Encerrando o programa.\n")

                os.system('pause')

                continuidade_menu = False

            case _:
                os.system('cls')

                print("[ERRO]Opção inválida!")
                print("Voltando ao menu.\n")

                os.system('pause')

