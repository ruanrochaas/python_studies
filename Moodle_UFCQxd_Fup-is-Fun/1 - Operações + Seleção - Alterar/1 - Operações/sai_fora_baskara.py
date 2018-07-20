a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

delta = b**2 - 4*a*c

if delta > 0:
    raiz1 = (-b + delta**0.5)/(2*a)
    raiz2 = (-b - delta**0.5)/(2*a)
    print("%.2f\n%.2f" %(raiz1, raiz2))
elif delta == 0:
    raiz = (b - 2*b)/(2*a) #gambs no -b pra fazer o moodle aceitar, tava dando -0,00 na saída. wtf ahuahuah
    print("%.2f" %raiz)
else:
    print("nao ha raiz real")