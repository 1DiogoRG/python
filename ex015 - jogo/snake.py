import pygame
import random

pygame.init()

largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
velocidade = 15

preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

def jogo():
    x, y = largura // 2, altura // 2
    dx, dy = 0, 0
    corpo = []
    comprimento = 1
    comida_x = random.randint(0, (largura - 10) // 10) * 10
    comida_y = random.randint(0, (altura - 10) // 10) * 10

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -10
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, 10
                elif evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -10, 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = 10, 0

        x += dx
        y += dy
        if x < 0 or x >= largura or y < 0 or y >= altura:
            rodando = False

        cabeca = [x, y]
        corpo.append(cabeca)
        if len(corpo) > comprimento:
            del corpo[0]

        if cabeca in corpo[:-1]:
            rodando = False

        if x == comida_x and y == comida_y:
            comprimento += 1
            comida_x = random.randint(0, (largura - 10) // 10) * 10
            comida_y = random.randint(0, (altura - 10) // 10) * 10

        tela.fill(preto)
        for parte in corpo:
            pygame.draw.rect(tela, verde, (*parte, 10, 10))
        pygame.draw.rect(tela, vermelho, (comida_x, comida_y, 10, 10))
        pygame.display.update()
        clock.tick(velocidade)

    pygame.quit()

jogo()
