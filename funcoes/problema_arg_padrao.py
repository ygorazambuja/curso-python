def fibonacci_mutavel(sequencia=[0, 1]):
    # Uso de mutáveis como valor Default
    # Lista não é Imutavel
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

    print(fibonacci_imutavel())
    pass
