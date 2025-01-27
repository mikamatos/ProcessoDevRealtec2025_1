import pygame
import time
import matplotlib.pyplot as plt

# aqui eu defini os parametros do sistema
taxa_resfriamento = 0.8  
taxa_aquecimento = 1.5  
temperatura_inicial = 10  
faixa_temperatura = [0, 15]  
T_desligar = 14  
T_ligar = 1  

# inicializando o pygame
pygame.init()

# configurando a tela
largura_tela = 800
altura_tela = 400
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Simulação de Controle de Temperatura")

# cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)

# fonte
fonte = pygame.font.SysFont(None, 36)

def desenhar_temperatura(temperatura, motor_ligado):
    screen.fill(BRANCO)

    # aqui desenha a barra de temperatura
    altura_barra = int((temperatura / faixa_temperatura[1]) * altura_tela)
    pygame.draw.rect(screen, AZUL, (largura_tela // 2 - 50, altura_tela - altura_barra, 100, altura_barra))

    # aqui para os limites
    texto_ligar = fonte.render(f"Liga: {T_ligar}°C", True, VERMELHO)
    texto_desligar = fonte.render(f"Desliga: {T_desligar}°C", True, VERMELHO)
    screen.blit(texto_ligar, (50, altura_tela - int((T_ligar / faixa_temperatura[1]) * altura_tela) - 20))
    screen.blit(texto_desligar, (50, altura_tela - int((T_desligar / faixa_temperatura[1]) * altura_tela) - 20))

    # para mostrar se o motor tá ligado ou não
    estado_motor = "Ligado" if motor_ligado else "Desligado"
    texto_estado_motor = fonte.render(f"Motor: {estado_motor}", True, PRETO)
    screen.blit(texto_estado_motor, (largura_tela // 2 - 100, 20))

    # e aqui para mostrar a temperatura atual
    texto_temperatura = fonte.render(f"Temperatura: {temperatura:.1f}°C", True, PRETO)
    screen.blit(texto_temperatura, (largura_tela // 2 - 150, 60))

    pygame.display.flip()

def simular_temperatura():
    temperatura = temperatura_inicial
    motor_ligado = False
    historico = []

    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # atualizando a temperatura
        if motor_ligado:
            temperatura -= taxa_resfriamento
            if temperatura <= T_ligar:
                motor_ligado = False
        else:
            temperatura += taxa_aquecimento
            if temperatura >= T_desligar:
                motor_ligado = True

        # para que a temp. não passe dos limites
        temperatura = max(faixa_temperatura[0], min(temperatura, faixa_temperatura[1]))

        # salva a temp. no histórico
        historico.append(temperatura)


        desenhar_temperatura(temperatura, motor_ligado)
        time.sleep(0.1)
        clock.tick(30)

    pygame.quit()
    return historico

def exibir_grafico(historico):
    plt.figure(figsize=(10, 5))
    plt.plot(historico, label="Temperatura", color="blue")
    plt.axhline(T_ligar, color="red", linestyle="--", label="Limite para Ligar")
    plt.axhline(T_desligar, color="green", linestyle="--", label="Limite para Desligar")
    plt.title("Variação da Temperatura ao Longo do Tempo")
    plt.xlabel("Tempo (segundos)")
    plt.ylabel("Temperatura (°C)")
    plt.legend()
    plt.grid()
    plt.show()

historico = simular_temperatura()
exibir_grafico(historico)
