num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

qtd_iguais = 0

if num1 == num2:
    qtd_iguais = 2
    
if num1 == num3:
    qtd_iguais = 2
    
if num3 == num2:
    qtd_iguais = 2

if num1 == num2 and num1 == num3:
    qtd_iguais = 3

print(qtd_iguais)