class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

    def __str__(self):
        return f'{self.vendedor}' + ' ' + f'{self.data}' + ' ' + f'{self.valor}'
        # return f'{self.data}'
