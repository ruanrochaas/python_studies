tam_vet = int(raw_input())
vetor = map(int, raw_input().split())

jedi = 0
sith = 0

for i in range(len(vetor)):
    if i < len(vetor)/2:
        jedi += vetor[i]
    else:
        sith += vetor[i]

if jedi > sith:
    print("Jedi")
elif jedi < sith:
    print("Sith")
else:
    print("Empate")