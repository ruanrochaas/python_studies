num1 = int(raw_input())
num2 = int(raw_input())

if num2 < num1:
    print("invalido")
else:
    soma = 0
    aux = num1
    while aux <= num2:
        if (aux % 2 == 0):
            soma += aux
        aux += 1
    print(soma)