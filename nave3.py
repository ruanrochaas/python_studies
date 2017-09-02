import random

class OVNI:
    def __init__(self, label, x, vida):
        self.label = label
        self.x = x
        self.vida = vida
        self.vivo = True

    def andar(self):
        if self.vivo == True:
            if(random.randint(0, 1) == 0):
                self.x = self.x - 1
            else:
                self.x = self.x + 1

    def apanhar(self, forca):
        if self.vivo == True:
            self.vida -= forca
            if self.vida <= 0:
                self.vivo = False

    
class Nave:
    def __init__(self, x, forca):
        self.x = x
        self.forca = forca

    def atirar(self, lista_ovni):
        for ovni in lista_ovni:
            if ovni.x == self.x:
                ovni.apanhar(self.forca)

    def mover(self, desl):
        self.x += desl


def testeImpressaoInimigos(objeto):
    if objeto.vivo:
        if objeto.x > 10:
            objeto.x = 9
            posInim1 = objeto.x
            posInim[posInim1] = "o"
        elif objeto.x < 1:
            objeto.x = 2
            posInim1 = objeto.x
            posInim[posInim1] = "o"
        else:
            posInim1 = objeto.x
            posInim[posInim1] = "o"
    else:
        if objeto.x > 10:
            objeto.x = 9
            posInim1 = objeto.x
            posInim[posInim1] = " "
        elif objeto.x < 1:
            objeto.x = 2
            posInim1 = objeto.x
            posInim[posInim1] = " "
        else:
            posInim1 = objeto.x
            posInim[posInim1] = " "


def testeImpressaoNave(objeto):
    if objeto.x > 10:
        return 10
    elif objeto.x < 1:
        return 1
    else:
        return objeto.x


def limparTela():
    print("\n" * 50)


nave = Nave(5, 1)
escolha = ""

lista = [OVNI("x", 2, 2), OVNI("y", 6, 3)]

limparTela()

while True:
    posInim = ["|"," "," "," "," "," "," "," "," "," "," ","|"]
    posNave = ["|"," "," "," "," "," "," "," "," "," "," ","|"]
    posTiro = ["|"," "," "," "," "," "," "," "," "," "," ","|"]

    testeImpressaoInimigos(lista[0])
    testeImpressaoInimigos(lista[1])
    posNave[testeImpressaoNave(nave)] = "^"
    
    inim = "".join(posInim)
    nave1 = "".join(posNave)

    print(inim, end = " ")
    print("Vida inimigo 1: %d" %lista[0].vida)
    
    if escolha == "a":
        posTiro[testeImpressaoNave(nave)] = "|"
        
    tiro = "".join(posTiro)
    
    print (tiro, end = " ")
    print("Vida inimigo 2: %d" %lista[1].vida)
    print(nave1)
    
    if not lista[0].vivo and not lista[1].vivo:
        print("\nVOCÊ GANHOU, IEEEEIIII!!")
        break
    escolha = input("d, e or a: ")
    if escolha == "d":
        nave.mover(1)
    elif escolha == "e":
        nave.mover(-1)
    elif escolha == "a":
        nave.atirar(lista)
    for x in lista:
        x.andar()
    
    limparTela()
