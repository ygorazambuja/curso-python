def tag_bloco(text, classe="success", inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{text}</{tag}>'
    pass


if __name__ == "__main__":
    print(tag_bloco('bloco'))
    print(tag_bloco('bloco', 'error', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou',  classe='error'))
    print(tag_bloco(inline=True, text='inline'))

    pass
