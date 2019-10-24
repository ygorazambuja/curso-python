class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome} ({self.idade} anos)'

    def is_adult(self):
        return (self.idade or 0) > 18
