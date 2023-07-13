def leitura():
    import menu
    menu.escreva('         PESSOAS CADASTRADAS     ')
    with open('\\base\\base.txt', "r+") as arquivo: # Editar caminho atual para caminho completo
        print(arquivo.read())

