class Data:

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    pass


d1 = Data()
d1.dia = 16
d1.mes = 10
d1.ano = 2019
print(d1)


d2 = Data()
d2.dia = 3
d2.mes = 7
d2.ano = 2419
print(d2)
