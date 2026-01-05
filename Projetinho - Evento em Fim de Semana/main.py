'''
CONJUNTOS SÃO SEM ORDEM, IMUTÁVEIS E NÃO INDEXADOS
'''

import os

inscritos_sabado = ["Albertinho", "Aninha", "Betinho", "Betinho", "Geraldinho", "Pedrinho", "Albertinho"]

inscritos_domingo = ["Azurinho", "Albertinho", "Clebinho", "Betinho", "Volvinho", "Volvinho", "Zurinho"]

controla_menu = True

def tratamento_listas(inscritos_sabado, inscritos_domingo):
    os.system("cls")

    print("Convertendo a lista de nomes para um conjunto, eliminando possíveis nomes repetidos indevidamente\n")

    conjunto_inscritos_sabado = set(inscritos_sabado)
    conjunto_inscritos_domingo = set(inscritos_domingo)

    print("Conjuntos Gravados!\n")

    print("Inscritos no Sábado:")
    for pessoa in conjunto_inscritos_sabado:
        print(pessoa)

    print("\nInscritos no Domingo:")
    for pessoa in conjunto_inscritos_domingo:
        print(pessoa)

    print("\nAgora, iremos mostrar os participantes que apareceram em ambos os dias.\n")

    os.system("pause")

    inscritos_ambos_dias(conjunto_inscritos_sabado, conjunto_inscritos_domingo)

def inscritos_ambos_dias(conjunto_inscritos_sabado, conjunto_inscritos_domingo):
    os.system("cls")

    print("Pessoas que aparecem em abos os dias:\n")

    for pessoa in conjunto_inscritos_sabado.intersection(conjunto_inscritos_domingo):
        print(pessoa)

    print("\nAgora, os inscritos que apareceram apenas no sábado.\n")

    os.system("pause")

    inscritos_apenas_sabado(conjunto_inscritos_sabado, conjunto_inscritos_domingo)

def inscritos_apenas_sabado(conjunto_inscritos_sabado, conjunto_inscritos_domingo):
    os.system("cls")

    print("Inscritos que foram apenas no sábado:")

    for pessoa in conjunto_inscritos_sabado.difference(conjunto_inscritos_domingo):
        print(pessoa)

    print("\nPor último, as pessoas que foram apenas em um dos dias (sábado ou domingo)\n")

    os.system("pause")

    inscritos_unico_dia(conjunto_inscritos_sabado, conjunto_inscritos_domingo)

def inscritos_unico_dia(conjunto_inscritos_sabado, conjunto_inscritos_domingo):
    os.system("cls")

    print("Pessoas que apenas foram em um dos dias:")

    for pessoa in conjunto_inscritos_sabado.symmetric_difference(conjunto_inscritos_domingo):
        print(pessoa)

    print("\n")

    os.system("pause")

    finalizacao_relatorio()

def finalizacao_relatorio():
    os.system("cls")

    print("Relatório do evento realizado.\n")

    print("Gostaria de repetir o relatório? (S/N)")
    
    escolha_menu = input()

    if(escolha_menu != "S" and escolha_menu != "s" and escolha_menu != "N" and escolha_menu != "n"):
        os.system("cls")

        print("[ERRO] Entrada inválida.")
        print("")


while(controla_menu == True):
    os.system("cls")

    print("--- DADOS DO EVENTO DO ÚLTIMO FIM DE SEMANA ---")
    print("Olá! Os dados do último evento realizado pela empresa foi disponibilizado.")
    print("Começaremos com um pequeno tratamento de dados para eliminar possíveis nomes duplicados em cada dia.\n")

    os.system("pause")

    tratamento_listas(inscritos_sabado, inscritos_domingo)
