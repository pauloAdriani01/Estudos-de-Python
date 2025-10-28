#Biblioteca importada para a limpeza do terminal
import os

#Funções para o programa funcionar
def funcConversaoMassa():
    #Comando para a limpeza do terminal no Windows
    _= os.system('cls') 

    print("Opção selecionada: Conversão de Massa")
    
    print("Qual é o valor em Quilogramas (Kg) que você gostaria de passar para Libras (lbs)?")
    
    valor = float(input())
    
    print(f"Valor selecionado para conversão: {valor:.2f}Kg") #fstring usado para formatar o float com 2 casas decimais

    resultado = valor * 2.20462

    print(f"O valor convertido é: {resultado:.2f}lbs\n")

    #Comando para dar uma pequena pausa no terminal do Windows
    _= os.system('pause')

    print("\nO que gostaria de fazer agora?\n")

    print("1 --> Outro cálculo de Quilogramas (Kg) para Libras (lbs)")
    print("2 --> Graus Celsius (ºC) para Graus Fahrenheit (Fº)")
    print("3 --> Voltar ao menu")
    print("4 --> Sair do programa")

    escolhaAcaoMenuMassa = int(input())

    match escolhaAcaoMenuMassa:
        case 1:
            funcConversaoMassa() 

        case 2:
            funcConversaoTemperatura()

        case 3:
            _= os.system('cls')

            print("Voltando ao menu...\n")

        case 4:
            _= os.system('cls')

            print("\nSaindo do programa... Até mais!")
            exit()

def funcConversaoTemperatura():
    _= os.system('cls')

    print("Opção selecionada: Conversão de Temperatura")

    print("Qual é o valor em Graus Celsius (ºC) que você gostaria de passar para Graus Fahrenheit (Fº)?")

    valor = float(input())

    print(f"Valor selecionado para conversão: {valor:.2f}ºC")

    resultado = (valor * 9/5) + 32

    print(f"O valor convertido é: {resultado:.2f}Fº\n")

    _= os.system('pause')

    print("\nO que gostaria de fazer agora?\n")

    print("1 --> Outro cálculo de Graus Celsius (ºC) para Graus Fahrenheit (Fº)")
    print("2 --> Quilogramas (Kg) para Libras (lbs)")
    print("3 --> Voltar ao menu")
    print("4 --> Sair do programa")

    escolhaAcaoMenuTemperatura = int(input())

    match escolhaAcaoMenuTemperatura:
        case 1:
            funcConversaoTemperatura()

        case 2:
            funcConversaoMassa() 

        case 3:
            _= os.system('cls')

            print("Voltando ao menu...\n")

        case 4:
            _= os.system('cls')

            print("\nSaindo do programa... Até mais!")
            exit()

#Execução do programa em si
print ("---Conversor de Unidades em Python---\n")

#Menu que se repete a cada função
while True:
    _= os.system('cls')

    #Variável para controle da escolha do usuário
    escolhaAcaoMenu = None
    
    #Variáveis para serem usadas nos cálculos
    valor = None
    resultado = None
    
    print("Bem-vindo(a) ao conversor de unidades!")
    print("Qual operação gostaria de fazer?\n")
    
    #Escolhas que o usuário pode fazer
    print("1 --> Quilogramas (Kg) para Libras (lbs)")
    print("2 --> Graus Celsius (ºC) para Graus Fahrenheit (Fº)")
    print("3 --> Sair do programa")
    
    escolhaAcaoMenu = int(input())
    
    match escolhaAcaoMenu:
        case 1:
            funcConversaoMassa()
        
        case 2:
            funcConversaoTemperatura()
        
        case 3:
            _= os.system('cls')

            print("\nSaindo do programa... Até mais!")
            break
        
        case _:
            _= os.system('cls')

            print("Opção inválida! Tente novamente.\n")
            
            _= os.system('pause')
        