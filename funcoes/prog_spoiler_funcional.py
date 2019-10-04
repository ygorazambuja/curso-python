def executar(funcao):
    if callable(funcao):
        funcao()
    pass


def bom_dia():
    print('bom dia')


def boa_tarde():
    print('boaa tarde')


if __name__ == "__main__":
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)
    pass
