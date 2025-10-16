numero1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador(+,-,*,/): ")
numero2 = float(input("Digite o segundo: "))
if operador == "+":
    soma = numero1 + numero2
    print("O resultado de {} + {} é = {}".format(numero1, numero2, soma))
elif operador == "-":
    subtracao = numero1 - numero2
    print("O resultado de {} - {} é = {}".format(numero1, numero2, subtracao))
elif operador == "*":
    multiplicacao = numero1 * numero2
    print("O resultado de {} * {} é = {}".format(numero1, numero2, multiplicacao))
elif operador == "/" :
    if numero2 == 0 or numero1 == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        divisao = numero1 / numero2
        print("O resultado de {} / {} é = {}".format(numero1, numero2, divisao))
else:
    print("Operador inválido! Por favor digite operador +, -, */")

