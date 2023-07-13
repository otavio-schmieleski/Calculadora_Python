import os
continua = True
lista = []
resultado = 0
Total_de_operacoes = 0

def soma():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float + numero_float
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def diminuir():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float - numero_float
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def multiplicacao():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float * numero_float
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def divisao():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float / numero_float
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def porcentagem():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float % numero_float
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def elevado_ao_quadrado():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float ** numero_float
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def raiz():
    global resultado
    global Total_de_operacoes
    resultado = numero2_float ** (1/2)
    os.system('cls')
    print(f"\nResultado: {resultado}\n")
    lista.append({'numero': numero2_float, 'numero_2' : numero_float, 'resultado': resultado})
    Total_de_operacoes += 1

def zerar_calculadora():
    global resultado
    global Total_de_operacoes
    os.system('cls')
    resultado = 0
    print(f"\nResultado: {resultado}\n")

def encerrar_calculadora():
    global resultado
    global Total_de_operacoes
    print("Calculadora encerrada")
    print(f"Total de Operacoes realizadas foi de: {Total_de_operacoes}")
    print(f"Este é o seu Historico de Calculos efetuados na calculadora:")
    for item in lista:
        print(item)
    

def opcoes():
    print("                 SELECIONE UMA OPCAO ABAIXO")
    print(" + ADICAO  |  - SUBTRACAO  |  * MULTIPLICACAO  |  / DIVISAO  | % PORCENTAGEM ")
    print()
    print(" X  x AO QUADRADO |  R RAIZ QUADRADA | C ZERAR | 0-> Encerrar calculadora") # verefica a opcao escolhida e faz a opracao
    print()
    global operacao
    operacao = input("qual operacao deseja realizar escolha alguma opcao acima (passe o sinal a frente da operacao) ").lower()

while continua:

    if Total_de_operacoes < 1:
        numero = input("informe um numero ")
        try:
            numero_float = float(numero)
        except ValueError:
            os.system('cls')
            print(f"\nResultado: {resultado}\n")
            print("voce nao informou um numero valido")
            continue

        opcoes()

        global numero2_float
        numero2 = input("informe um numero ")
        try:
            numero2_float = float(numero2)
        except ValueError:
            os.system('cls')
            print(f"\nResultado: {resultado}\n")
            print("voce nao informou um numero valido")
            continue

    else:

        opcoes()

        if operacao == "r":
            numero2_float = float(resultado)
            raiz()
            continue
        elif operacao == "c":
            zerar_calculadora()
            continue
        elif operacao == "0":
            os.system('cls')
            encerrar_calculadora()
            break

        numero = input("informe um numero ")
        try:
            numero_float = float(numero)
        except ValueError:
            os.system('cls')
            print(f"\nResultado: {resultado}\n")
            print("voce nao informou um numero valido")
            continue

        numero2_float = float(resultado)

    if operacao == "+" : # faz as operacoes escolhidas
        soma()
    elif operacao == "-" :
        diminuir()
    elif operacao == "*" :
        multiplicacao()
    elif operacao == "/" :
        divisao()
    elif operacao == "%":
        porcentagem()
    elif operacao == "x":
        elevado_ao_quadrado()
    elif operacao == "r":
       raiz()
    elif operacao == "c":
        zerar_calculadora()
    elif operacao == "0" :
        encerrar_calculadora()
        continua = False
    else:
        print("nao escolheu nenhuma opcao valida")

    os.system('cls')
    print(f"\nResultado: {resultado}\n")