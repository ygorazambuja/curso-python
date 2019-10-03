def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a+b+c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == "__main__":

    tupla_nums = (1, 2, 3)
    lista_nums = [1, 2, 3]

    # packing
    print(soma_2(2, 3))
    print(soma_3(2, 3, 4))
    print(soma_n(1, 2, 3, 4, 5))

    # unpacking
    print(soma_n(*tupla_nums))
    print(soma_n(*lista_nums))
    pass
