import pygame
from pygame.locals import QUIT, KEYUP, K_RETURN
from jogo.gui.cores import CORES

class TelaTutorial:
    def __init__(self):
        self.display = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Tutorial")
        self.fonte = pygame.font.SysFont("Courier New", 24)
        self.instrucoes = [
            "Seja Bem-vindo ao Jogo!",
            "",
            "Instruções:",
            "1. Use as teclas W, A, S, D para mover o personagem.",
            "2. O objetivo é simples, recuperar o tesouro!",
            "3. Encontre e use poções para melhorar suas habilidades.",
            "4. Cuidado com as armadilhas espalhadas pelo mapa, elas podem causar",
                "dano ao seu personagem.",
            "5. Talvez você encontre algumas adversidades pelo caminho...",
            "6. Pressione 'P' para salvar o jogo.",
            "7. Pressione 'Q' para sair do jogo.",
            "",
            "Agora é com você, pressione Enter para começar sua aventura!"
        ]

    def renderizar(self):
        self.display.fill(CORES.preto)
        for i, linha in enumerate(self.instrucoes):
            texto = self.fonte.render(linha, True, CORES.branco)
            self.display.blit(texto, (20, 30 * i + 20))
        pygame.display.update()

def mostrar_tutorial():
    tutorial = TelaTutorial()
    tutorial.renderizar()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                return False
            if evento.type == KEYUP and evento.key == K_RETURN:
                return True
        pygame.time.Clock().tick(30)
