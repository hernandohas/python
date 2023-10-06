# Classes e Obejetos

class Martelo:
    def __init__(self, peso, tamanho):
        self.peso = peso
        self.tamanho = tamanho    

    def martelar(self):
        print("Martelando.... Descendo a marretada com Peso: ", self.peso)

meu_martelo = Martelo(15, 40)
meu_martelo.martelar()

meu_martelo_2 = Martelo(22, 60)
meu_martelo_2.martelar()