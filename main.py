#Começo da calculadora

#importações
import os

   #Funções
#Limpar_tela: serve para "Limpar a tela"
def limpar_tela():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / Mac
        os.system("clear")

#Letreiro: serve para especificar para o usuario qual opção escolher
def letreiro():
    print(25*"=")
    print("Programa principal".center(23, ' '))
    print(25*"=")
    print("[1] Calculadora")
    print("[2] Desafios matematicos")
    print("[3] Sair")
    print(25*"=")

#Letreiro2: Serve para especificar para o usuario que operação ele deve escolher
def operacao():
    print(25*"=")
    print("Operações".center(23, ' '))
    print(25*"=")
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print(25*"=")



#Estrutura de repetição
while True:  #apenas um while True para manter o programa funcionando para testar

    letreiro() #letreiro
    resposta_menu = str(input("Qual você deseja :")).strip() # pegando a resposta do usuario

    #Estrutura de Condição:
     #Primeira condição refere-se a calculadora
    if resposta_menu == "1":  
        limpar_tela() #limpando tela
        operacao() #opeções

        resposta_operacao = str(input("Qual você deseja :")).strip() # pegando a resposta do usuario
        while not resposta_operacao.isdigit():
            limpar_tela()
            letreiro()
            print("Você não digitou uma escolha do menu")
            resposta_operacao = str(input("Qual você deseja :")).strip()






    #FUTURO
    elif resposta_menu == "2":
        print("Em desenvolvimento")

    elif resposta_menu == "3":
        limpar_tela()
        print("Fechando programa.")
        break

    else:
        print(f"{resposta_menu} não existe.")

    break #quebrar a estrutura de repetição