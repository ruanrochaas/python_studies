capacidade = int(raw_input())
qtd_embarc = 0
movimentacao = 0
cap_max = 2*capacidade

while qtd_embarc < cap_max:
    movimentacao = int(raw_input())
    qtd_embarc += movimentacao
    
    if qtd_embarc == 0:
        print("vazio")
    elif qtd_embarc < capacidade:
        print("ainda cabe")
    elif (qtd_embarc >= capacidade) and (qtd_embarc < cap_max):
        print("lotado")
    elif qtd_embarc >= cap_max:
        print("hora de partir")