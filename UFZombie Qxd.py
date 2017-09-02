import pygame
import time

pygame.init()

branco = (255,255,255)
preto = (0,0,0)
verde = (0,255,0)
vermelho = (255,0,0)

larguraDaTela = 800
alturaDaTela = 600

telaDeJogo = pygame.display.set_mode((larguraDaTela,alturaDaTela)) #cria a tela e diz o tamanho dela
pygame.display.set_caption("UFZombie Qxd") #nome do jogo

fps = 30

clock = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 50)
fonte2 = pygame.font.SysFont(None, 35)

def mensagem(msg, cor):
    textoNaTela = fonte.render(msg, True, cor)
    telaDeJogo.blit(textoNaTela, [larguraDaTela/2, alturaDaTela/2])

def relogio(msg, cor):
    textoRel = fonte2.render(msg, True, cor)
    telaDeJogo.blit(textoRel, [50,50])

def lacoJogo():
    fimDeJogo = False
    
    #player
    posicao_x = larguraDaTela/2
    posicao_y = alturaDaTela/2
    mudarPosicao_x = 0
    mudarPosicao_y = 0

    #inimigo1
    posicaoInimigo_x = 600
    posicaoInimigo_y = 400
    mudarPosicaoInimigo_x = 0
    mudarPosicaoInimigo_y = 0

    #inimigo2
    posicaoInimigo2_x = 100
    posicaoInimigo2_y = 100
    mudarPosicaoInimigo2_x = 0
    mudarPosicaoInimigo2_y = 0
    
    while not fimDeJogo:
        relogio(str(int(round(pygame.time.get_ticks()/1000))), branco)
        pygame.display.update()
        for evento in pygame.event.get(): #recebe todos os eventos que acontecem (botões apertados, posição do mouse etc)
            if evento.type == pygame.QUIT:
                fimDeJogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mudarPosicao_x = -5
                elif evento.key == pygame.K_RIGHT:
                    mudarPosicao_x = 5
                elif evento.key == pygame.K_UP:
                    mudarPosicao_y = -5
                elif evento.key == pygame.K_DOWN:
                    mudarPosicao_y = 5
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and mudarPosicao_x == -5:
                    mudarPosicao_x = 0
                elif evento.key == pygame.K_RIGHT and mudarPosicao_x == 5:
                    mudarPosicao_x = 0
                elif evento.key == pygame.K_UP and mudarPosicao_y == -5:
                    mudarPosicao_y = 0
                elif evento.key == pygame.K_DOWN and mudarPosicao_y == 5:
                    mudarPosicao_y = 0
        
        
        
        
        posicao_x += mudarPosicao_x
        posicao_y += mudarPosicao_y
            
        if posicao_x > 780:
            posicao_x = 780
        elif posicao_x < 0:
            posicao_x = 0
        if posicao_y > 580:
            posicao_y = 580
        elif posicao_y < 0:
            posicao_y = 0
        
        if abs(posicao_x - posicaoInimigo_x) > 50:
            if posicao_x > posicaoInimigo_x:
                mudarPosicaoInimigo_x = 6
            elif posicao_x < posicaoInimigo_x:
                mudarPosicaoInimigo_x = -6
        else:
            if posicao_x > posicaoInimigo_x:
                mudarPosicaoInimigo_x = 4
            elif posicao_x < posicaoInimigo_x:
                mudarPosicaoInimigo_x = -4
        
        if abs(posicao_y - posicaoInimigo_y) > 50:
            if posicao_y > posicaoInimigo_y:
                mudarPosicaoInimigo_y = 6
            elif posicao_y < posicaoInimigo_y:
                mudarPosicaoInimigo_y = -6
        else:
            if posicao_y > posicaoInimigo_y:
                mudarPosicaoInimigo_y = 4
            elif posicao_y < posicaoInimigo_y:
                mudarPosicaoInimigo_y = -4
        
        if abs(posicao_x - posicaoInimigo2_x) > 50:
            if posicao_x > posicaoInimigo2_x:
                mudarPosicaoInimigo2_x = 6
            elif posicao_x < posicaoInimigo2_x:
                mudarPosicaoInimigo2_x = -6
        else:
            if posicao_x > posicaoInimigo2_x:
                mudarPosicaoInimigo2_x = 4.5
            elif posicao_x < posicaoInimigo2_x:
                mudarPosicaoInimigo2_x = -4.5
        
        if abs(posicao_y - posicaoInimigo2_y) > 50:
            if posicao_y > posicaoInimigo2_y:
                mudarPosicaoInimigo2_y = 6
            elif posicao_y < posicaoInimigo2_y:
                mudarPosicaoInimigo2_y = -6
        else:
            if posicao_y > posicaoInimigo2_y:
                mudarPosicaoInimigo2_y = 4.5
            elif posicao_y < posicaoInimigo2_y:
                mudarPosicaoInimigo2_y = -4.5

        posicaoInimigo_x += mudarPosicaoInimigo_x
        posicaoInimigo_y += mudarPosicaoInimigo_y
        
        posicaoInimigo2_x += mudarPosicaoInimigo2_x
        posicaoInimigo2_y += mudarPosicaoInimigo2_y
        
        telaDeJogo.fill(preto)
        pygame.draw.rect(telaDeJogo, branco, [posicao_x,posicao_y,20,20]) #desenha o jogador
        pygame.draw.rect(telaDeJogo, verde, [posicaoInimigo_x,posicaoInimigo_y,20,20]) #desenha o inimigo1
        pygame.draw.rect(telaDeJogo, verde, [posicaoInimigo2_x,posicaoInimigo2_y,20,20]) #desenha o inimigo2
        
        
        pygame.display.update()

        if  (posicaoInimigo_x == posicao_x or posicaoInimigo2_x == posicao_x) and (posicaoInimigo_y == posicao_y or posicaoInimigo2_y == posicao_y):
            break
        
        clock.tick(fps)

lacoJogo()

mensagem("Você foi comido!", vermelho)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
