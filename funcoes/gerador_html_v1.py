
# Parametro Default = Javascript


def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    #Testes (Assertions)
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'

    assert tag_bloco('Impossível Excluir!', 'error') == \
        '<div class="error">Impossível Excluir!</div>'

    pass
