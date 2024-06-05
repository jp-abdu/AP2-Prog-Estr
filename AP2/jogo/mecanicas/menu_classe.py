from ..gui.menu_classe import MenuClasse

from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.paladino import Paladino

import pygame

def selecionar_classe():
    menu = MenuClasse()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                match MenuClasse.mapear_clique(pos):
                    case "Guerreiro":
                        return Guerreiro
                    case "Paladino":
                        return Paladino

        menu.renderizar()
