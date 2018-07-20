def palindromo(num):
    aux = num
    invert = 0
    
    while  aux != 0:
        invert = invert * 10 + aux % 10
        aux = aux // 10
    
    if num == invert:
        return True
    else:
        return False

if palindromo(int(raw_input())):
    print(1)
else:
    print(0)

