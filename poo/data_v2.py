class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    pass


d1 = Data(16, 10, 2019)
print(d1)


d2 = Data(3, 7, 2099)
print(d2)
