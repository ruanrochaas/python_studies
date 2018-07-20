tam_vet = int(raw_input())
vetor = map(int, raw_input().split())

som_pares = 0
som_impares = 0

for ele in vetor:
    if ele % 2 == 0:
        som_pares += ele
    else:
        som_impares += ele

if som_pares > som_impares:
    print("rebeldes")
elif som_pares < som_impares:
    print("soldados")
else:
    print("empate")