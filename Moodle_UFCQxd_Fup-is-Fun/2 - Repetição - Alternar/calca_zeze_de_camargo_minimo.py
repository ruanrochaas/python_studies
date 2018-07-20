cont = 0
menor = 0
while cont < 5:
    num = int(raw_input())
    if cont == 0:
        menor = num
    elif num < menor:
        menor = num
    cont += 1
print(menor)