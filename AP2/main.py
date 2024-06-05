from jogo.mecanicas.mecanicas import loop
from jogo.mecanicas import arquivo
import pygame
from tutorial import mostrar_tutorial

def iniciar_jogo():
    pygame.init()

def encerrar_jogo():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar_jogo()
    if not arquivo.existe_save():
        if not mostrar_tutorial():
            return
    loop()
    encerrar_jogo()

if __name__ == "__main__":
    main()
