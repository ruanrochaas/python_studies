nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
trab = float(raw_input())

menor = nota1
meio = 0
maior = 0

if nota2 < menor:
    menor = nota2
if nota3 < menor:
    menor = nota3

nota = (nota1 + nota2 + nota3 - menor + trab)/3

if nota >= 7:
    print("Aprovado com %.1f" %nota)
else:
    print("Final com %.1f" %nota)