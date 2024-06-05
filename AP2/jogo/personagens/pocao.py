# pocao.py
import random
from ..gui.cores import CORES
from .personagem import Personagem


class Pocao(Personagem):
    def __init__(self, tesouro):

        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0) or (x == y == tesouro.posicao):
                break
            
        self.char = "%"
        self.cor = CORES.verde
        self.posicao = [x, y]

    def aplicar_efeito(self, aventureiro):
        efeito = random.choice(["dobrar_vida", "aumentar_forca", "aumentar_defesa"])
        if efeito == "dobrar_vida":
            aventureiro.vida *= 2
        elif efeito == "aumentar_forca":
            aventureiro.forca += 15
        elif efeito == "aumentar_defesa":
            aventureiro.defesa += 10
    
    def alterar_posicao(self, nova_pos):
        self.posicao = nova_pos

    def carregar(self, dados):
        self.posicao = dados["posicao"]

    def info(self):
        return {"posicao": self.posicao}