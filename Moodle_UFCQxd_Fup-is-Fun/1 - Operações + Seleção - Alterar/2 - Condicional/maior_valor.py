num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())
num4 = int(raw_input())

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4

print(maior)