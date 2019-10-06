def fibonacci_mutavel(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


def fibonacci_imutavel(sequencia=(0, 1)):
    return sequencia + (sequencia[-1] + sequencia[-2],)


if __name__ == "__main__":
    inicio = fibonacci_mutavel()
    print(inicio, id(inicio))
    print(fibonacci_mutavel(inicio))
    restart = fibonacci_mutavel()
    print(restart, id(restart))

    pass
