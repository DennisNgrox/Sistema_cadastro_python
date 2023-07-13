def cadastrar(nome, idade):
    import base
    with open('C:\\Users\\Ageri\\Desktop\\SCRIPTS\\Python\\cadastro\\base\\base.txt', "a") as arquivo:
        a = arquivo.write(f'{nome} : {idade}\n')
        return f'Nome {nome} com a idade {idade}, cadastrado'
        arquivo.close()
