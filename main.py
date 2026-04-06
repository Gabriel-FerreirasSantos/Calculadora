#Começo da calculadora


#Funções
    #Letreiro: serve para deixar o programa estético para o usuario
def letreiro():
    print(25*"=")
    print("Programa principal".center(23, ' '))
    print(25*"=")
    print("[1] Calculadora")
    print("[2] Desafios matematicos")
    print("[3] Sair")
    print(25*"=")



#Estrutura de repetição
while True:  #apenas um while True para manter o programa funcionando para testar

    letreiro() #letreiro
    resposta = str(input("Qual você deseja :")).strip() # pegando a resposta do usuario

    #Estrutura de Condição:
    if resposta == "1":
        print("Número 1")

    elif resposta == "2":
        print("Número 2")

    elif resposta == "3":
        print("Número 3")

    else:
        print(f"{resposta} não existe.")

    break #quebrar a estrutura de repetição