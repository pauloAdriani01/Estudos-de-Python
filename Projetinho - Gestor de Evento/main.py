'''
CONJUNTOS SÃO SEM ORDEM, IMUTÁVEIS E NÃO INDEXADOS
'''

import os

#Controle do menu principal
continuidade_programa = True

#Conjuntos que armazenarão as informações do evento
dia_1 = set()
dia_2 = set()

def registrar_presenca_primeiro_dia(dia_1, dia_2):
    os.system("cls")

    print("Opção selecionada: Registrar presença no primeiro dia")

    print("ATENÇÃO: Dados errados não podem ser modificados.\n")

    print("Qual é o ID do participante?")
    ID_participante = detectar_erro_entrada_inteiro()

    #Caso inserir um valor não válido para o ID
    if(ID_participante == None):
        return dia_1

    #Conferência se o ID já existe
    for participante in dia_1:
        if(ID_participante == participante[0]):
            os.system("cls")

            print("[ERRO]ID já existente.")
            print("Reiniciando o programa.\n")
            os.system("pause")

            return None

    for participante in dia_2:
        if(ID_participante == participante[0]):
            os.system("cls")

            print("[ERRO]ID já existente.")
            print("Reiniciando o programa.\n")
            os.system("pause")

            return None

    print("\nComo é o nome do participante?")
    nome_participante = input()

    info_participante = (ID_participante, nome_participante)

    os.system("cls")

    #Informações do participante adicionadas
    dia_1.add(info_participante)

    print("Informações do Participante Adicionado:\n")

    print(f"ID: {info_participante[0]}")
    print(f"Nome: {info_participante[1]}\n")

    print("Voltando ao menu principal.")
    os.system("pause")

def registrar_presenca_segundo_dia(dia_1, dia_2):
    os.system("cls")

    print("Opção selecionada: Registrar presença no segundo dia")

    print("ATENÇÃO: Dados errados não podem ser modificados.\n")

    print("Qual é o ID do participante?")
    ID_participante = detectar_erro_entrada_inteiro()

    #Caso inserir um valor não válido para o ID
    if(ID_participante == None):
        return dia_2

    #Conferência se o ID já existe
    for participante in dia_1:
        if(ID_participante == participante[0]):
            os.system("cls")

            print("[ERRO]ID já existente.")
            print("Reiniciando o programa.\n")
            os.system("pause")

            return None

    for participante in dia_2:
        if(ID_participante == participante[0]):
            os.system("cls")

            print("[ERRO]ID já existente.")
            print("Reiniciando o programa.\n")
            os.system("pause")

            return None

    print("\nComo é o nome do participante?")
    nome_participante = input()

    info_participante = (ID_participante, nome_participante)

    os.system("cls")

    #Informações do participante adicionadas
    dia_2.add(info_participante)

    print("Informações do Participante Adicionado:\n")

    print(f"ID: {info_participante[0]}")
    print(f"Nome: {info_participante[1]}\n")

    print("Voltando ao menu principal.")
    os.system("pause")

def ver_lista_presenca(dia_1, dia_2):
    escolha_menu = 0

    cont_participantes_dia_1 = 0
    cont_participantes_dia_2 = 0

    os.system("cls")

    #Testa se há participantes em ao menos 1 das listas
    for participante in dia_1:
        cont_participantes_dia_1 += 1

    for participante in dia_2:
        cont_participantes_dia_2 += 1

    #Condições para seguir com essa opção do programa
    if(cont_participantes_dia_1 == 0 and cont_participantes_dia_2 == 0):
        print("[ERRO]Não há participantes no sistema")
        print("Voltando ao menu principal\n")

        os.system("pause")

        return None

    elif(cont_participantes_dia_1 != 0 and cont_participantes_dia_2 == 0):
        print("ATENÇÃO: Não há participantes registrados no segundo dia\n")

    elif(cont_participantes_dia_1 == 0 and cont_participantes_dia_2 != 0):
        print("ATENÇÃO: Não há participantes registrados no primeiro dia\n")

    print("Opção selecionada: Ver lista de presença")
    print("Como você gostaria de ver?\n")

    print("1 --> Participantes presentes em um dia")
    print("2 --> Participantes presentes nos dois dias")
    print("3 --> Participantes presentes apenas no primeiro dia")
    print("4 --> Participantes presentes apenas no segundo dia")
    print("5 --> Retornar ao menu principal\n")

    escolha_menu = detectar_erro_entrada_inteiro()

    if(escolha_menu != None):
        match (escolha_menu):
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                os.system("cls")

                print("Opção selecionada: Retornar ao menu principal\n")

                print("Voltando...")
                os.system("pause")

                return None

            case _:
                os.system("cls")

                print("[ERRO] Opção inválida.")
                print("Reiniciando o programa.\n")

                os.system("pause")

                return None

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
    print("4 --> Remover um participante")
    print("5 --> Sair\n")

    escolha_menu = detectar_erro_entrada_inteiro()

    if(escolha_menu != None):
        match (escolha_menu):
            case 1:
                registrar_presenca_primeiro_dia(dia_1, dia_2)

            case 2:
                registrar_presenca_segundo_dia(dia_1, dia_2)

            case 3:
                ver_lista_presenca(dia_1, dia_2)

            case 4:
                pass

            case 5:
                pass

            case _:
                os.system("cls")

                print("[ERRO] Opção inválida.")
                print("Reiniciando o programa.\n")

                os.system("pause")

while(continuidade_programa == True):
    menu_principal()