from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' -  (Concluída) ' if self.feito else '')


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())}) tarefas pendente(s)'


def main():

    casa = Projeto('Tarefas de Casa')

    casa.add('Lavar Pratos')
    casa.add('Lavar pratos')

    print(casa)
    casa.procurar('Lavar Pratos').concluir()
    for tarefa in casa.tarefas:
        print(f' - {tarefa}')
    print(casa)


if __name__ == "__main__":
    main()
