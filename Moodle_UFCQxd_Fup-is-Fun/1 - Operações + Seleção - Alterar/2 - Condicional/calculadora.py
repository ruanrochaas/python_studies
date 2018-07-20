num1 = int(raw_input())
num2 = int(raw_input())
operador = raw_input()

res = 0

if operador == "/" and num2 == 0:
    print("invalida")
else:
    if operador == "+":
        res = num1 + num2
    elif operador == "-":
        res = num1 - num2
    elif operador == "*":
        res = num1 * num2
    elif operador == "/":
        res = num1 / num2
    print(res)