x, n = map(int, raw_input().split())
lista = map(int, raw_input().split())

cont = 0

for ele in lista:
    if ele == x:
        cont += 1

print(cont)