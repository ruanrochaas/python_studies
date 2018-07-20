qtd_comp = int(input())

cont = 0
venc = -1
pont_venc = -1
while cont < qtd_comp:
    arrem1, arrem2 = map(int, raw_input().split())
    pont_temp = abs(arrem1 - arrem2)
    if arrem1 < 10 or arrem2 < 10:
        cont += 1
        continue
    if venc == -1 or pont_temp < pont_venc:
        venc = cont
        pont_venc = pont_temp
    cont += 1

if venc == -1:
    print("sem ganhador")
else:
    print(venc)