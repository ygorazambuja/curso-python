from datetime import datetime


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        pass

    def is_adult(self):
        pass


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario=0):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return f'{self.nome}  {self.idade} {self.salario}'


class Cliente(Pessoa):
    def __init__(self, nome, idade, compras=[]):
        super().__init__(nome, idade)
        self.compras = compras

    def registrar_compra(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        data = self.compras[-1].data
        pass

    def total_compras(self):
        pass
    pass


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

    def __str__(self):
        return f'{self.vendedor}' + ' ' + f'{self.data}' + ' ' + f'{self.valor}'
        # return f'{self.data}'


if __name__ == "__main__":
    vendedor = Vendedor('Ygor', 25, 2000)
    cliente = Cliente('Izadora', 25)

    compra = Compra(vendedor, datetime.now(), 200)

    print(compra)
    pass
