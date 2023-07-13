def cadastrar(nome, idade):
    import base
    with open('\\base\\base.txt', "a") as arquivo: # Editar caminho atual para caminho completo
        a = arquivo.write(f'{nome} : {idade}\n')
        return f'Nome {nome} com a idade {idade}, cadastrado'
        arquivo.close()
