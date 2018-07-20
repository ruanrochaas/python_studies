nota1 = int(raw_input())
nota2 = int(raw_input())
nota3 = int(raw_input())

menor = nota1
meio = 0
maior = 0

if nota2 <= menor:
    meio = menor
    menor = nota2
else:
    meio = nota2

if nota3 <= menor:
    maior = meio
    meio = menor
    menor = nota3
elif nota3 <= meio:
    maior = meio
    meio = nota3
else:
    maior = nota3

print(meio)