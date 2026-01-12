'''
CONJUNTOS SÃO SEM ORDEM, IMUTÁVEIS E NÃO INDEXADOS
'''

import os

#Controle do menu principal
continuidade_programa = True

#Conjuntos que armazenarão as informações do evento
dia_1 = set()
dia_2 = set()

def registrar_presença_primeiro_dia(dia_1):
    os.system("cls")

    print("ATENÇÃO: Dados errados não podem ser modificados.\n")

    print("Qual é o ID do participante?")
    ID_participante = detectar_erro_entrada_inteiro()


    print("Como é o nome do participante?")
    nome_participante = input()

    os.system("cls")



def detectar_erro_entrada_inteiro():
    try:
        escolha = int(input())

    except:
        os.system("cls")

        print("[ERRO] Entrada inválida.")
        print("Reiniciando o programa.\n")

        os.system("pause")

        return None

    else:
        return escolha

def menu_principal():
    escolha_menu = 0

    os.system("cls")

    print("Bem-vindo ao Sistema Gestor do seu Evento.")
    print("Como gostaria de prosseguir?\n")

    print("1 --> Registrar presença no primeiro dia")
    print("2 --> Registrar presença no segundo dia")
    print("3 --> Ver lista de presença")
    print("4 --> Sair\n")

    escolha_menu = detectar_erro_entrada_inteiro()

    if(escolha_menu != None):
        match (escolha_menu):
            case 1:
                registrar_presença_primeiro_dia(dia_1)

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case _:
                os.system("cls")

                print("[ERRO] Opção inválida.")
                print("Reiniciando o programa.\n")

                os.system("pause")

while(continuidade_programa == True):
    menu_principal()