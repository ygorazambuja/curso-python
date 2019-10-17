class Carro():
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    # def acelerar(self, delta=5):
    #     if((self.velocidade_atual + delta) > self.velocidade_maxima):
    #         self.velocidade_atual = self.velocidade_maxima
    #     else:
    #         self.velocidade_atual += delta

    #     return(self.velocidade_atual)
    #     pass

    # def frear(self, delta):
    #     if((self.velocidade_atual - delta) < 0):
    #         self.velocidade_atual = 0
    #     else:
    #         self.velocidade_atual -= delta

    #     return(self.velocidade_atual)

    def acelerar(self, delta=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual


if __name__ == "__main__":
    carro = Carro(180)

    for _ in range(25):
        print(carro.acelerar(8))

    for _ in range(10):
        print(carro.frear(delta=20))
    pass
