from .aventureiro import Aventureiro

class Secreta(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.vida = 200
        self.forca = 30
        self.defesa = 30
        self.char = "S"
        self.status = "Você é um aventureiro secreto! Comece a explorar!"