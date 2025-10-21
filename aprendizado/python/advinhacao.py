# Importação de bibliotecas necessárias
import random
import time
import os
import sys

# Inicialização do Sistema
print("Iniciando o sistema de adivinhação...")
time.sleep(1)

print("Selecione o dado que será utilizado: ")
print("1 - Dado de 6 lados")
print("2 - Dado de 10 lados")
print("3 - Dado de 20 lados")
print("4 - Dado de 100 lados")

# Loop de controle de jogo
at_work = True
while at_work:

    # Leitura da escolha do usuário
    dado = int(input("Digite o número correspondente ao dado desejado: "))

    if dado == 1:
        lados = 6
    elif dado == 2:
        lados = 10
    elif dado == 3:
        lados = 20
    elif dado == 4:
        lados = 100
    else:
        print("Opção inválida. Encerrando o programa.")
        sys.exit()

    # Geração do número aleatório

    numero_secreto = random.randint(1, lados)
    print(f"Dado de {lados} lados selecionado. Um número entre 1 e {lados} foi gerado.")
    time.sleep(1)
    print("Tente adivinhar o número gerado!")

    tentativas = 0

    # Loop de tentativas

    for tentativas in range (10):
        
        print(f"\nTentativa número ", tentativas)
        palpite = input("Digite o palpite aqui: ")
        palpite = int(palpite)
        tentativas += 1

        if tentativas > 10 and palpite != numero_secreto:
            print (f"Infelizmente você não foi capaz de acertar, o número era: ", numero_secreto)
        elif palpite == numero_secreto:
            print ("Parabéns! Você acertou!")
            break

    # Reiniciador de Loop
    
    cont = input(str("Deseja jogar novamente? (s/n)"))
    
    try:
        if cont.lower() == 's':
            pass
        else:
            at_work = False
    except Exception as e:
        print(e)
