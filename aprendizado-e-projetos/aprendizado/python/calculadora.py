# Importações 
import sys
import math

# Criação de lista vazia
hist = []

# Inicialização do sistema
print("Bem vindo à Calculadora!")

at_work = True
while at_work:

    # Entrada de dados
    opr = input("Digite a operação (+, -, *, /, sqrt, pow) ou 'exit' para sair: ")
        
    if opr == 'exit':
        sys.exit()

    num1 = float(input("Digite o primeiro número: "))
        
    if opr != 'sqrt':
        num2 = float(input("Digite o segundo número: "))
        

    # Classe de operador
    class Operador:
        '''
    Classe que contém métodos estáticos para operações matemáticas básicas: 
    soma, subtração, multiplicação, divisão, raiz quadrada e potência.

    O método estático (@staticmethod) indica que o método não depende do estado da 
    instância da classe e pode ser chamado diretamente na classe sem criar um objeto.
        '''
        
        @staticmethod
        def sum(num1, num2):
            return num1 + num2

        @staticmethod
        def sub(num1, num2):
            return num1 - num2

        @staticmethod
        def mult(num1, num2):
            return num1 * num2

        @staticmethod
        def divs(num1, num2):
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero!")
            return num1 / num2

        @staticmethod
        def rad(num1):
            if num1 < 0:
                raise ValueError("Não é possível tirar raiz de números negativos!")
            return math.sqrt(num1)

        @staticmethod
        def pow(num1, num2):
            return num1 ** num2

    # Processamento de dados

    try:
        if opr == '+':
            res = Operador.sum(num1, num2)
        elif opr == '-':
            res = Operador.sub(num1, num2)
        elif opr == '*':
            res = Operador.mult(num1, num2)
        elif opr == '/':
            res = Operador.divs(num1, num2)
        elif opr == 'sqrt':
            res = Operador.rad(num1)
        elif opr == 'pow':
            res = Operador.pow(num1, num2)
        else:
            print("Operação inválida.")
            sys.exit()
        print(f"O resultado é: {res}")
        
        # Armazenar histórico
        hist.append(f"{num1} {opr} {num2 if opr != 'sqrt' else ''} = {res}")

        # Reportando erros
    except Exception as e:
        print(e)

    # Exibir histórico
    ver_hist = input("Deseja ver o histórico de operações e fechar o sistema? (s/n): ")
    if ver_hist.lower() == 's':
        print(f"Histórico de operações: \n")
        for record in hist:
            print(record)
        at_work = False

