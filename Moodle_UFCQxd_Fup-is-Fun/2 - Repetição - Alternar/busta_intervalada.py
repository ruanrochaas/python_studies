tam_vet = raw_input()
interv = map(int, raw_input().split())
vetor = map(int, raw_input().split())

cont = 0

for ele in vetor:
    if ele >= interv[0] and ele <= interv[1]:
        cont += 1

print(cont)