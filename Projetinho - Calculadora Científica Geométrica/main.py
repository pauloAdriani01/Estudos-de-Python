import os
import math

#Declaração das Funções
def menuPrincipal():
    _= os.system('cls')

    print("--- CALCULADORA CIENTÍFICA GEOMÉTRICA EM PYTHON ---\n")

    print("Olá! Seja bem-vind@ à calculadora!")
    print("Qual função você deseja utilizar?")
    print("(digite o número correspondente à função desejada)\n")

    print("1 - Cálculo de Área (Polígonos)")
    print("2 - Cálculo de Área (Círculos)")
    print("3 - Teorema de Pitágoras")
    print("4 - Encerrar Programa")

    #Testa se o usuário digitou um valor inválido para o tipo especificado
    try:
        escolhaUsuario = int(input("\n"))

    except ValueError:
        print("[ERRO]Entrada inválida! Tente novamente.\n")

        _= os.system('pause')

        menuPrincipal()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaPoligonos()

def calcularAreaPoligonos():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (POLÍGONOS) ---\n")

    print("Qual é o seu polígono?\n")
    print("1 - Triângulo")
    print("2 - Quadrado")
    print("3 - Retângulo")
    print("4 - Losango")
    print("5 - Trapézio")
    print("6 - Parelologramo")
    print("7 - Voltar ao Menu Principal\n")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        _= os.system('cls')

        print("[ERRO]Entrada inválida!")

        print("Como você gostaria de proceder?\n")

        print("1 - Voltar a Função de Cálculo de Área (Polígonos)")
        print("2 - Voltar ao Menu Principal")
        print("3 - Encerrar Programa\n")

        try:
            escolhaUsuario = int(input())

        except ValueError:
            print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

            _= os.system('pause')

            exit()

        else:
            match escolhaUsuario:
                case 1:
                    calcularAreaPoligonos()

                case 2:
                    menuPrincipal()

                case 3:
                    print("\nEncerrando Programa...\n")

                    _= os.system('pause')

                    exit()

                case _:
                    print("\n[ERRO]Entrada inválida! Voltando ao Menu Principal\n")

                    _= os.system('pause')

                    menuPrincipal()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaTriangulo()

def calcularAreaTriangulo():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (TRIÂNGULO) ---\n")

    print("Com qual triângulo você deseja trabalhar?\n")

    print("1 - Triângulo (Sabendo Base e Altura)")
    print("2 - Triângulo Retângulo")
    print("3 - Triângulo Equilátero")
    print("4 - Voltar ao Menu de Cálculo de Área (Polígonos)\n")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        print("\n[ERRO]Entrada inválida! Voltando ao Menu de Cálculo de Área (Polígonos)\n")

        _= os.system('pause')

        calcularAreaPoligonos()

    else:
        match escolhaUsuario:
            case 1:
                

#Programa
menuPrincipal()