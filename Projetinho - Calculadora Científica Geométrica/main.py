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

            case 2:
                calcularAreaCirculos()

            case 3:
                pass

            case 4:
                _= os.system('cls')

                print("Obrigado por utilizar a calculadora!")
                print("Encerrando Programa...\n")

                _= os.system('pause')

                exit()

            case _:
                print("\n[ERRO]Entrada inválida! Tente novamente.\n")

                _= os.system('pause')

                menuPrincipal()


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

            case 2:
                calcularAreaQuadrado()

            case 3:
                calcularAreaRetangulo()

            case 4:
                calcularAreaLosango()

            case 5:
                calcularAreaTrapezio()

            case 6:
                calcularAreaParelologramo()

            case 7:
                menuPrincipal()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit()

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
                _= os.system('cls')

                print("Qual é o valor da base do seu triângulo?")
                baseTriangulo = float(input())

                print("\nQual é o valor da altura do seu triângulo?")
                alturaTriangulo = float(input())

                resultado = (baseTriangulo * alturaTriangulo) / 2

                _= os.system('cls')

                print(f"\nA área de seu triângulo é: {resultado:.2f}\n")

                print("Como você gostaria de proceder?\n")

                print("1 - Calcular outro triângulo")
                print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

                try:
                    escolhaUsuario = int(input())

                except ValueError:
                    print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                    _= os.system('pause')

                    exit()

                else:
                    match escolhaUsuario:
                        case 1:
                            calcularAreaTriangulo()

                        case 2:
                            calcularAreaPoligonos()

                        case _:
                            print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                            _= os.system('pause')

                            exit()
            
            case 2:
                _= os.system('cls')

                print("Qual é o valor do seu primeiro cateto (adjascente)?")
                catetoAdjascente = float(input())

                print("\nQual é o valor do seu segundo cateto (oposto)?")
                catetoOposto = float(input())

                resultado = (catetoAdjascente * catetoOposto) / 2

                print(f"\nA área de seu triângulo é: {resultado:.2f}\n")

                print("Como você gostaria de proceder?\n")

                print("1 - Calcular outro triângulo")
                print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

                try:
                    escolhaUsuario = int(input())

                except ValueError:
                    print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                    _= os.system('pause')

                    exit()

                else:
                    match escolhaUsuario:
                        case 1:
                            calcularAreaTriangulo()

                        case 2:
                            calcularAreaPoligonos()

                        case _:
                            print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                            _= os.system('pause')

                            exit()

            case 3:
                _= os.system('cls')

                print("Qual é o valor do lado do seu triângulo equilátero?")
                ladoTriangulo = float(input())

                #Utilização da biblioteca math para o cálculo da raíz quadrada
                resultado = (ladoTriangulo ** 2) * (math.sqrt(3)) / 4

                print(f"\nA área de seu triângulo é: {resultado:.2f}\n")

                print("Como você gostaria de proceder?\n")

                print("1 - Calcular outro triângulo")
                print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

                try:
                    escolhaUsuario = int(input())

                except ValueError:
                    print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                    _= os.system('pause')

                    exit()

                else:
                    match escolhaUsuario:
                        case 1:
                            calcularAreaTriangulo()

                        case 2:
                            calcularAreaPoligonos()

                        case _:
                            print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                            _= os.system('pause')

                            exit()

            case 4:
                calcularAreaPoligonos()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit()

def calcularAreaQuadrado():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (QUADRADO) ---\n")

    print("Qual é o valor do lado do seu quadrado?")
    ladoQuadrado = float(input())

    resultado = ladoQuadrado ** 2

    print(f"\nA área de seu quadrado é: {resultado:.2f}\n")

    print("Como você gostaria de proceder?\n")

    print("1 - Calcular outro quadrado")
    print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

        _= os.system('pause')

        exit()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaQuadrado()

            case 2:
                calcularAreaPoligonos()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit() 

def calcularAreaRetangulo():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (RETÂNGULO) ---\n")

    print("Qual é o valor da base do seu retângulo?")
    baseRetangulo = float(input())

    print("\nQual é o valor da altura do seu retângulo?")
    alturaRetangulo = float(input())

    resultado = baseRetangulo * alturaRetangulo

    print(f"\nA área de seu retângulo é: {resultado:.2f}\n")

    print("Como você gostaria de proceder?\n")

    print("1 - Calcular outro retângulo")
    print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

        _= os.system('pause')

        exit()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaRetangulo()

            case 2:
                calcularAreaPoligonos()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit()

def calcularAreaLosango():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (LOSANGO) ---\n")

    print("Qual é o valor da diagonal maior do seu losango?")
    diagonalMaior = float(input())

    print("\nQual é o valor da diagonal menor do seu losango?")
    diagonalMenor = float(input())

    resultado = (diagonalMaior * diagonalMenor) / 2

    print(f"\nA área de seu losango é: {resultado:.2f}\n")

    print("Como você gostaria de proceder?\n")

    print("1 - Calcular outro losango")
    print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

        _= os.system('pause')

        exit()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaLosango()

            case 2:
                calcularAreaPoligonos()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit()

def calcularAreaTrapezio():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (TRAPÉZIO) ---\n")

    print("Qual é o valor da base maior do seu trapézio?")
    baseMaior = float(input())

    print("\nQual é o valor da base menor do seu trapézio?")
    baseMenor = float(input())

    print("\nQual é o valor da altura do seu trapézio?")
    alturaTrapezio = float(input())

    resultado = ((baseMaior + baseMenor) * alturaTrapezio) / 2

    print(f"\nA área de seu trapézio é: {resultado:.2f}\n")

    print("Como você gostaria de proceder?\n")

    print("1 - Calcular outro trapézio")
    print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

        _= os.system('pause')

        exit()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaTrapezio()

            case 2:
                calcularAreaPoligonos()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit()

def calcularAreaParelologramo():
    _= os.system('cls')

    print("--- OPÇÃO SELECIONADA: CÁLCULO DE ÁREA (PARELOLOGRAMO) ---\n")

    print("Qual é o valor da base do seu parelelogramo?")
    baseParelologramo = float(input())

    print("\nQual é o valor da altura do seu parelelogramo?")
    alturaParelologramo = float(input())

    resultado = baseParelologramo * alturaParelologramo

    print(f"\nA área de seu parelelogramo é: {resultado:.2f}\n")

    print("Como você gostaria de proceder?\n")
    print("1 - Calcular outro parelelogramo")
    print("2 - Voltar ao Menu de Cálculo de Área (Polígonos)")

    try:
        escolhaUsuario = int(input())

    except ValueError:
        print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

        _= os.system('pause')

        exit()

    else:
        match escolhaUsuario:
            case 1:
                calcularAreaParelologramo()

            case 2:
                calcularAreaPoligonos()

            case _:
                print("\n[ERRO]Entrada inválida! Encerrando Programa\n")

                _= os.system('pause')

                exit()

def calcularAreaCirculos():
    pass

#Programa
menuPrincipal()
